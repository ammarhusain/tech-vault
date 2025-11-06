"""
Configuration for RL training of language models.
"""

class TrainingConfig:
    # Model configuration
    model_name = "microsoft/phi-1_5"  # We'll use this as our base model
    max_length = 512
    batch_size = 4
    
    # RL training hyperparameters
    learning_rate = 2e-5
    eps_clip = 0.2  # PPO clipping parameter
    value_loss_coef = 0.5
    entropy_coef = 0.01
    max_grad_norm = 0.5
    num_epochs = 4  # Number of epochs per batch of experiences
    
    # KL divergence settings
    target_kl = 0.02
    kl_penalty_coef = 0.1
    
    # Training loop settings
    num_episodes = 1000
    max_steps_per_episode = 100
    
    # Experience buffer settings
    buffer_size = 1000
    min_buffer_size = 100
    
    # Advantage estimation
    gamma = 0.99  # Discount factor
    lambda_ = 0.95  # GAE parameter
    
    # Reward scaling
    reward_scaling = 1.0
    reward_clip = 10.0
    
    # Dataset configuration
    dataset_name = "anthropic/hh-rlhf"  # We'll use Anthropic's RLHF dataset
    split = "train"
    
    # Logging
    log_interval = 10
    eval_interval = 100
    save_interval = 500