"""
Implementation of the PPO agent for language model training.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, List, Tuple
import numpy as np
from dataclasses import dataclass

@dataclass
class Experience:
    """Container for a single experience tuple."""
    state_ids: torch.Tensor
    action_ids: torch.Tensor
    attention_mask: torch.Tensor
    rewards: torch.Tensor
    values: torch.Tensor
    log_probs: torch.Tensor
    advantages: torch.Tensor = None
    returns: torch.Tensor = None

class ExperienceBuffer:
    """Buffer for storing and processing experiences."""
    
    def __init__(self, buffer_size: int):
        self.buffer_size = buffer_size
        self.experiences: List[Experience] = []
        
    def add(self, experience: Experience):
        """Add an experience to the buffer."""
        if len(self.experiences) >= self.buffer_size:
            self.experiences.pop(0)
        self.experiences.append(experience)
        
    def clear(self):
        """Clear the buffer."""
        self.experiences = []
        
    def compute_advantages(self, gamma: float, lambda_: float):
        """
        Compute advantages using Generalized Advantage Estimation (GAE).
        
        Args:
            gamma: Discount factor
            lambda_: GAE parameter
        """
        for exp in self.experiences:
            # Get rewards and values
            rewards = exp.rewards
            values = exp.values
            
            # Initialize advantages and returns
            advantages = torch.zeros_like(rewards)
            returns = torch.zeros_like(rewards)
            
            # Compute GAE
            last_gae = 0
            for t in reversed(range(len(rewards))):
                if t == len(rewards) - 1:
                    next_value = 0
                else:
                    next_value = values[t + 1]
                
                delta = rewards[t] + gamma * next_value - values[t]
                advantages[t] = delta + gamma * lambda_ * last_gae
                last_gae = advantages[t]
                
                # Compute returns
                returns[t] = advantages[t] + values[t]
            
            exp.advantages = advantages
            exp.returns = returns
            
    def get_batch(self, batch_size: int) -> List[Experience]:
        """Get a random batch of experiences."""
        indices = np.random.choice(len(self.experiences), batch_size, replace=False)
        return [self.experiences[i] for i in indices]

class PPOAgent:
    """
    PPO agent for training language models with RL.
    """
    
    def __init__(
        self,
        model,
        learning_rate: float,
        eps_clip: float,
        value_loss_coef: float,
        entropy_coef: float,
        max_grad_norm: float,
        target_kl: float
    ):
        self.model = model
        self.optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
        
        self.eps_clip = eps_clip
        self.value_loss_coef = value_loss_coef
        self.entropy_coef = entropy_coef
        self.max_grad_norm = max_grad_norm
        self.target_kl = target_kl
        
    def compute_action_log_probs(
        self,
        logits: torch.Tensor,
        action_ids: torch.Tensor,
        attention_mask: torch.Tensor
    ) -> torch.Tensor:
        """
        Compute log probabilities of taken actions.
        
        Args:
            logits: Model logits [batch_size, seq_len, vocab_size]
            action_ids: Chosen action IDs [batch_size, seq_len]
            attention_mask: Attention mask [batch_size, seq_len]
            
        Returns:
            Log probabilities of chosen actions
        """
        # Shift logits and actions for next-token prediction
        shift_logits = logits[..., :-1, :].contiguous()
        shift_actions = action_ids[..., 1:].contiguous()
        shift_mask = attention_mask[..., 1:].contiguous()
        
        # Compute log probabilities
        log_probs = F.log_softmax(shift_logits, dim=-1)
        token_log_probs = log_probs.gather(-1, shift_actions.unsqueeze(-1)).squeeze(-1)
        
        # Mask padding tokens
        token_log_probs = token_log_probs * shift_mask
        
        return token_log_probs
    
    def train_step(
        self,
        experience: Experience,
        old_logits: torch.Tensor
    ) -> Dict[str, float]:
        """
        Perform a single PPO training step.
        
        Args:
            experience: Experience tuple
            old_logits: Logits from old policy
            
        Returns:
            Dictionary of training metrics
        """
        # Get model outputs
        outputs = self.model(
            input_ids=experience.state_ids,
            attention_mask=experience.attention_mask,
            return_value=True
        )
        
        new_logits = outputs["logits"]
        new_values = outputs["values"].squeeze(-1)
        
        # Compute log probabilities
        new_log_probs = self.compute_action_log_probs(
            new_logits,
            experience.action_ids,
            experience.attention_mask
        )
        old_log_probs = self.compute_action_log_probs(
            old_logits,
            experience.action_ids,
            experience.attention_mask
        )
        
        # Compute ratio and clipped ratio
        ratio = torch.exp(new_log_probs - old_log_probs.detach())
        clipped_ratio = torch.clamp(ratio, 1 - self.eps_clip, 1 + self.eps_clip)
        
        # Compute policy loss
        advantages = experience.advantages
        policy_loss_unclipped = ratio * advantages
        policy_loss_clipped = clipped_ratio * advantages
        policy_loss = -torch.min(policy_loss_unclipped, policy_loss_clipped).mean()
        
        # Compute value loss
        value_loss = F.mse_loss(new_values, experience.returns)
        
        # Compute entropy bonus
        probs = F.softmax(new_logits, dim=-1)
        entropy = -(probs * F.log_softmax(new_logits, dim=-1)).sum(-1).mean()
        
        # Compute total loss
        total_loss = (
            policy_loss
            + self.value_loss_coef * value_loss
            - self.entropy_coef * entropy
        )
        
        # Compute KL divergence
        kl = self.model.compute_kl_divergence(
            experience.state_ids,
            experience.attention_mask,
            old_logits
        )
        
        # Check if we should early stop due to KL divergence
        if kl > 1.5 * self.target_kl:
            return {
                "policy_loss": policy_loss.item(),
                "value_loss": value_loss.item(),
                "entropy": entropy.item(),
                "kl": kl.item(),
                "early_stop": True
            }
        
        # Optimize
        self.optimizer.zero_grad()
        total_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.max_grad_norm)
        self.optimizer.step()
        
        return {
            "policy_loss": policy_loss.item(),
            "value_loss": value_loss.item(),
            "entropy": entropy.item(),
            "kl": kl.item(),
            "early_stop": False
        }
    
    def get_action(
        self,
        state_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        temperature: float = 1.0
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Generate an action (response) given a state (prompt).
        
        Args:
            state_ids: Input token IDs
            attention_mask: Attention mask
            temperature: Sampling temperature
            
        Returns:
            Tuple of (action_ids, values, logits)
        """
        with torch.no_grad():
            action_ids, values = self.model.generate_with_value(
                input_ids=state_ids,
                attention_mask=attention_mask,
                do_sample=True,
                temperature=temperature
            )
            
            # Get logits for the generated sequence
            outputs = self.model(action_ids, return_value=False)
            logits = outputs["logits"]
            
        return action_ids, values, logits