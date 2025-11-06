"""
Implementation of the policy and value networks for RL training.
"""

import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Dict, Tuple, Optional
import os

class ValueHead(nn.Module):
    """Value function head that estimates the expected return of a state."""
    
    def __init__(self, hidden_size: int):
        super().__init__()
        self.value_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            nn.Tanh(),
            nn.Linear(hidden_size, 1)
        )
        
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        """
        Args:
            hidden_states: Hidden states from the language model [batch_size, seq_len, hidden_size]
            
        Returns:
            Value estimates [batch_size, seq_len, 1]
        """
        return self.value_head(hidden_states)

class RLModel(nn.Module):
    """
    Wrapper around the language model that adds RL-specific functionality.
    """
    
    def __init__(self, model_name: str):
        super().__init__()
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Add padding token if it doesn't exist
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
        # Set padding side to left for decoder-only models
        self.tokenizer.padding_side = 'left'
            
        # Initialize value head
        self.value_head = ValueHead(self.model.config.hidden_size)
        
    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        labels: Optional[torch.Tensor] = None,
        return_value: bool = True
    ) -> Dict[str, torch.Tensor]:
        """
        Forward pass through both policy and value networks.
        
        Args:
            input_ids: Input token IDs [batch_size, seq_len]
            attention_mask: Attention mask [batch_size, seq_len]
            labels: Labels for language modeling [batch_size, seq_len]
            return_value: Whether to compute value estimates
            
        Returns:
            Dictionary containing model outputs and optionally value estimates
        """
        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels,
            output_hidden_states=return_value,
            return_dict=True
        )
        
        result = {
            "logits": outputs.logits,
            "loss": outputs.loss if labels is not None else None
        }
        
        if return_value:
            # Get the last hidden states for value estimation
            last_hidden = outputs.hidden_states[-1]
            values = self.value_head(last_hidden)
            result["values"] = values
            
        return result
    
    def generate_with_value(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        max_length: int = 512,
        **kwargs
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Generate text while also computing value estimates.
        
        Args:
            input_ids: Input token IDs [batch_size, seq_len]
            attention_mask: Attention mask [batch_size, seq_len]
            max_length: Maximum sequence length
            
        Returns:
            Tuple of (generated_ids, value_estimates)
        """
        # Store original inputs for value computation later
        original_inputs = input_ids.clone()
        original_mask = attention_mask.clone() if attention_mask is not None else None
        
        # Generate text
        generated_ids = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=max_length,
            pad_token_id=self.tokenizer.pad_token_id,
            **kwargs
        )
        
        # Compute values for the generated sequence
        with torch.no_grad():
            outputs = self.model(
                input_ids=generated_ids,
                output_hidden_states=True,
                return_dict=True
            )
            values = self.value_head(outputs.hidden_states[-1])
            
        return generated_ids, values
    
    def compute_kl_divergence(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        old_logits: torch.Tensor
    ) -> torch.Tensor:
        """
        Compute KL divergence between old and new policy.
        
        Args:
            input_ids: Input token IDs [batch_size, seq_len]
            attention_mask: Attention mask [batch_size, seq_len]
            old_logits: Logits from old policy [batch_size, seq_len, vocab_size]
            
        Returns:
            KL divergence value
        """
        with torch.no_grad():
            new_logits = self.model(input_ids, attention_mask).logits
            
        # Compute KL divergence
        old_probs = torch.nn.functional.softmax(old_logits, dim=-1)
        new_probs = torch.nn.functional.softmax(new_logits, dim=-1)
        
        kl = torch.sum(old_probs * (torch.log(old_probs) - torch.log(new_probs)), dim=-1)
        # Mask out padding tokens
        kl = kl * attention_mask
        
        return kl.mean()
    
    def save_pretrained(self, path: str):
        """Save both the model and value head."""
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)
        torch.save(self.value_head.state_dict(), f"{path}/value_head.pt")
        
    @classmethod
    def from_pretrained(cls, path: str):
        """Load both the model and value head."""
        model = cls(path)
        value_head_path = f"{path}/value_head.pt"
        if os.path.exists(value_head_path):
            model.value_head.load_state_dict(torch.load(value_head_path))
        return model