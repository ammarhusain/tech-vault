"""
Data handling utilities for RL training.
"""

from datasets import load_dataset
from typing import Dict, List, Tuple
import torch
from transformers import PreTrainedTokenizer

class RLHFDataHandler:
    """
    Handler for RLHF datasets that provides prompts and computes rewards.
    """
    
    def __init__(
        self,
        dataset_name: str,
        split: str,
        tokenizer: PreTrainedTokenizer,
        max_length: int
    ):
        self.dataset = load_dataset(dataset_name, split=split)
        self.tokenizer = tokenizer
        self.max_length = max_length
        
    def extract_prompt(self, chosen_text: str) -> str:
        """
        Extract the prompt from the chosen text.
        In the Anthropic dataset, prompts are typically prefixed with "Human: "
        and responses with "Assistant: ".
        """
        if "Human: " in chosen_text:
            return chosen_text.split("Human: ")[1].split("Assistant: ")[0].strip()
        return chosen_text  # fallback if format is different
        
    def get_batch(self, batch_size: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Get a batch of prompts and their corresponding preferred responses.
        
        Args:
            batch_size: Number of examples to retrieve
            
        Returns:
            Tuple of (input_ids, attention_mask)
        """
        # Sample random indices
        indices = torch.randint(0, len(self.dataset), (batch_size,))
        
        # Get examples
        examples = [self.dataset[idx.item()] for idx in indices]
        
        # Extract prompts from chosen responses
        prompts = [self.extract_prompt(ex["chosen"]) for ex in examples]
        
        # Tokenize
        encodings = self.tokenizer(
            prompts,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        )
        
        return encodings["input_ids"], encodings["attention_mask"]
    
    def compute_reward(
        self,
        prompt: str,
        response: str,
        chosen: str,
        rejected: str
    ) -> float:
        """
        Compute reward for a generated response based on similarity to preferred response.
        
        This is a simple reward function based on token overlap with the chosen response
        and negative overlap with the rejected response. In practice, you would want
        a more sophisticated reward model.
        
        Args:
            prompt: The input prompt
            response: The generated response
            chosen: The preferred response from the dataset
            rejected: The rejected response from the dataset
            
        Returns:
            Reward value
        """
        # Extract assistant responses from chosen/rejected texts
        if "Assistant: " in chosen:
            chosen_response = chosen.split("Assistant: ")[1].strip()
        else:
            chosen_response = chosen
            
        if "Assistant: " in rejected:
            rejected_response = rejected.split("Assistant: ")[1].strip()
        else:
            rejected_response = rejected
        
        # Tokenize all texts
        response_tokens = set(self.tokenizer.tokenize(response))
        chosen_tokens = set(self.tokenizer.tokenize(chosen_response))
        rejected_tokens = set(self.tokenizer.tokenize(rejected_response))
        
        # Compute overlaps
        chosen_overlap = len(response_tokens.intersection(chosen_tokens))
        rejected_overlap = len(response_tokens.intersection(rejected_tokens))
        
        # Compute reward as difference in overlaps
        reward = (chosen_overlap - rejected_overlap) / max(len(response_tokens), 1)
        
        return reward
    
    def batch_compute_rewards(
        self,
        prompts: List[str],
        responses: List[str]
    ) -> torch.Tensor:
        """
        Compute rewards for a batch of responses.
        
        Args:
            prompts: List of input prompts
            responses: List of generated responses
            
        Returns:
            Tensor of reward values
        """
        rewards = []
        
        # Get random examples from dataset for comparison
        indices = torch.randint(0, len(self.dataset), (len(prompts),))
        examples = [self.dataset[idx.item()] for idx in indices]
        
        for prompt, response, example in zip(prompts, responses, examples):
            reward = self.compute_reward(
                prompt,
                response,
                example["chosen"],
                example["rejected"]
            )
            rewards.append(reward)
        
        return torch.tensor(rewards)
    
    def decode_responses(
        self,
        response_ids: torch.Tensor,
        attention_mask: torch.Tensor
    ) -> List[str]:
        """
        Decode token IDs back to text, handling padding appropriately.
        
        Args:
            response_ids: Token IDs [batch_size, seq_len]
            attention_mask: Attention mask [batch_size, seq_len]
            
        Returns:
            List of decoded responses
        """
        responses = []
        
        for ids, mask in zip(response_ids, attention_mask):
            # Only decode tokens that aren't padding
            valid_ids = ids[mask.bool()]
            decoded = self.tokenizer.decode(valid_ids, skip_special_tokens=True)
            responses.append(decoded)
            
        return responses