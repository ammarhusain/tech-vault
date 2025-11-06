"""
Main training script for RL fine-tuning of language models.
"""

import torch
from src.model import RLModel
from src.ppo_agent import PPOAgent, ExperienceBuffer, Experience
from src.data_handler import RLHFDataHandler
from configs.training_config import TrainingConfig
import wandb
from tqdm import tqdm
import os

def main():
    # Initialize wandb
    config = {attr: getattr(TrainingConfig, attr) for attr in dir(TrainingConfig) 
             if not attr.startswith('__')}
    wandb.init(project="llm-rl-tutorial", config=config)
    
    # Set up device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Initialize model
    print("Initializing model...")
    model = RLModel(TrainingConfig.model_name).to(device)
    
    # Initialize data handler
    print("Loading dataset...")
    data_handler = RLHFDataHandler(
        dataset_name=TrainingConfig.dataset_name,
        split=TrainingConfig.split,
        tokenizer=model.tokenizer,
        max_length=TrainingConfig.max_length
    )
    
    # Initialize PPO agent
    print("Setting up PPO agent...")
    agent = PPOAgent(
        model=model,
        learning_rate=TrainingConfig.learning_rate,
        eps_clip=TrainingConfig.eps_clip,
        value_loss_coef=TrainingConfig.value_loss_coef,
        entropy_coef=TrainingConfig.entropy_coef,
        max_grad_norm=TrainingConfig.max_grad_norm,
        target_kl=TrainingConfig.target_kl
    )
    
    # Initialize experience buffer
    buffer = ExperienceBuffer(TrainingConfig.buffer_size)
    
    # Training loop
    print("Starting training...")
    global_step = 0
    
    for episode in range(TrainingConfig.num_episodes):
        # Get batch of prompts
        state_ids, attention_mask = data_handler.get_batch(TrainingConfig.batch_size)
        state_ids = state_ids.to(device)
        attention_mask = attention_mask.to(device)
        
        # Generate responses and get values
        action_ids, values, logits = agent.get_action(
            state_ids,
            attention_mask,
            temperature=1.0
        )
        
        # Decode responses
        prompts = data_handler.tokenizer.batch_decode(
            state_ids,
            skip_special_tokens=True
        )
        responses = data_handler.tokenizer.batch_decode(
            action_ids,
            skip_special_tokens=True
        )
        
        # Compute rewards
        rewards = data_handler.batch_compute_rewards(prompts, responses)
        rewards = rewards.to(device)
        
        # Create experience
        experience = Experience(
            state_ids=state_ids,
            action_ids=action_ids,
            attention_mask=attention_mask,
            rewards=rewards,
            values=values,
            log_probs=None  # Will be computed during training
        )
        
        # Add to buffer
        buffer.add(experience)
        
        # Only train if we have enough experiences
        if len(buffer.experiences) >= TrainingConfig.min_buffer_size:
            # Compute advantages
            buffer.compute_advantages(
                gamma=TrainingConfig.gamma,
                lambda_=TrainingConfig.lambda_
            )
            
            # Train for multiple epochs on collected experiences
            for _ in range(TrainingConfig.num_epochs):
                # Get random batch of experiences
                batch = buffer.get_batch(TrainingConfig.batch_size)
                
                # Train on batch
                metrics = []
                for exp in batch:
                    metric = agent.train_step(exp, logits)
                    metrics.append(metric)
                    
                    if metric["early_stop"]:
                        break
                
                # Log metrics
                avg_metrics = {
                    k: sum(m[k] for m in metrics) / len(metrics)
                    for k in metrics[0].keys()
                    if k != "early_stop"
                }
                wandb.log(avg_metrics, step=global_step)
                
            # Clear buffer after training
            buffer.clear()
        
        global_step += 1
        
        # Log episode info
        if episode % TrainingConfig.log_interval == 0:
            print(f"Episode {episode}/{TrainingConfig.num_episodes}")
            print(f"Average reward: {rewards.mean().item():.3f}")
            
            # Log example conversation
            example_idx = 0
            wandb.log(
                {
                    "example_conversation": wandb.Table(
                        columns=["prompt", "response", "reward"],
                        data=[[
                            prompts[example_idx],
                            responses[example_idx],
                            rewards[example_idx].item()
                        ]]
                    )
                },
                step=global_step
            )
        
        # Save checkpoint
        if episode % TrainingConfig.save_interval == 0:
            checkpoint_dir = f"checkpoints/episode_{episode}"
            os.makedirs(checkpoint_dir, exist_ok=True)
            model.save_pretrained(checkpoint_dir)
            print(f"Saved checkpoint to {checkpoint_dir}")

if __name__ == "__main__":
    main()