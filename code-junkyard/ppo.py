import gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv
import torch.nn as nn

# Create the environment
env = gym.make('CartPole-v1')
env = DummyVecEnv([lambda: env])

# Define a custom neural network policy
policy_kwargs = dict(
    net_arch=[dict(pi=[64, 64], vf=[64, 64])],
    activation_fn=nn.Tanh
)

# Initialize the PPO agent
model = PPO(
    "MlpPolicy",
    env,
    learning_rate=0.0003,
    n_steps=2048,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    gae_lambda=0.95,
    clip_range=0.2,
    policy_kwargs=policy_kwargs,
    verbose=1
)

# Train the agent
total_timesteps = 25000
model.learn(total_timesteps=total_timesteps)

# Evaluate the trained agent
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Mean reward: {mean_reward:.2f} +/- {std_reward:.2f}")

# Test the trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render()
    if dones:
        obs = env.reset()

env.close()