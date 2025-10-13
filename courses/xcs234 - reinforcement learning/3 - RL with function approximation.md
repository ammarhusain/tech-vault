---
created: 2022-08-09-Tuesday 15:22
modified: 2023-03-10-Friday 23:15
---

Slides - [[courses/xcs234 - reinforcement learning/attachments/Mod3_Slides.pdf]]

# 3.1 Introduction to Value Function Approximation

# Value Function Approximation
- In module 2 we learned how to learn a good policy from experience
- Given known dynamics and reward models, and a tabular representation
	- Discussed how to do policy evaluation and then control (value iteration and policy iteration)
- Given no models, and a tabular representation
	- Discussed how to do policy evaluation (MC/TD) and then control (MC, SARSA, Q-learning)
- So far, have been assuming we can represent the value function or state-action value function as a vector/ matrix
	- Tabular representation
- Many real world problems have enormous state and/or action spaces so tabular representation is insufficient

## Motivation for Function Approximation
- Don’t want to have to explicitly store or learn for every single state a:
	- Dynamics or reward model
	- Value
	- State-action value
	- Policy
- Want more compact representation that generalizes across state or states and actions
- Reduce memory, comoutation and / or experience needed to compute & store P, R / V / Q / $\pi$

 ![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 1.png]]

- Many possible function approximators including:
	- Linear combinations of features
	- Neural networks
	- Decision trees
	- Nearest neighbors
	- Fourier/ wavelet bases
- In this class we will focus on function approximators that are differentiable (Why?)
- Two very popular classes of differentiable function approximators
	- Linear feature representations (Today)
	- Neural networks (Next lecture)

Policy evaluation is a simpler yet critical building block for designing control algorithms

**Value function approximation for Polixy Evaluation with an Oracle**

- First assume we could query any state s and an oracle would return the true value for $V^{\pi}(s)$
- Similar to supervised learning: assume given $(s, V^{\pi}(s))$ pairs
- The objective is to find the best approximate representation of $V^{\pi}$ given a particular parameterized function $Vˆ(s;w)$

![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 3.png]]

However the problem is that we do not have access to this Oracle true value function $V^{\pi }(s)$
Recall that in model-free policy evaluation:

- Following a fixed policy $\pi$ (or had access to prior data)
- Goal is to estimate $V^{\pi}$ and/or $Q^{\pi}$
Maintained a lookup table to store estimates $V^{\pi}$ and/or $Q^{\pi}$
Updated these estimates after each episode (Monte Carlo methods) or after each step (TD methods)
Now : in value function approximation, change the estimate update step to include fitting the function approximator

---

---

# 3.2 Reinforcement Learning with Linear Value Function Approximator

## Mc Learning for Policy Evaluation with Linear Vfa

Use a feature vector to represent a state s

![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 4.png]]
![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 5.png]]
![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 6.png]]

## Mc Learning for Policy Evaluation with Linear Vfa Convergence Guarantees

Some meh theoretical stuff

## Td Learning for Policy Evaluation with Linear Vfa

![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 7.png]]
In value function approximation, target is $r + γV^{π} (s' ; w)$, a biased and approximated estimate of the true value $V^π (s)$
3 forms of approximation:

 1. Sampling
 2. Bootstrapping
 3. Value function approximation

![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 8.png]]
![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 9.png]]

Monte carlo update will have high variance, low bias - larger update size
TD learning update will have low variance, high bias - smaller update size

## Mc and Td Control with Linear Vfa (VALUE Function APPROXIMATION)

**Control using Value Function Approximation**

- Use value function approximation to represent state-action values $Q^{\pi} (s, a; w) ≈ Q^{π}$
- Interleave
	- Approximate policy evaluation using value function approximation
	- Perform $\epsilon$-greedy policy improvement
- Can be unstable. Generally involves intersection of the following:
	1. Function approximation
	2. Bootstrapping
	3. Off-policy learning

![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 10.png]]
![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 11.png]]

$G_t$ is the discounted sum of rewards
![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 12.png]]
**Convergence of TD methods with VFA**

- Informally, updates involve doing an (approximate) Bellman backup followed by best trying to fit underlying value function to a particular feature representation
- Bellman operators are contractions, but value function approximation fitting can be an expansion
| Algorithm           | Tabular | Linear VFA | Nonlinear VFA |
| ------------------- | ------- | ---------- | ------------- |
| Monte-Carlo Control | yes     | yes        | depends       |
| Sarsa               | yes     | yes        | depends       |
| Q-learning          | yes     | no         | depends       |

---

## 3.3 Deep Reinforcement Learning

## Function Approximation with Deep Neural Networks

2 axes along which RL algorithms operate
|                                      | tabular   (small countable state) | large state space (usually a continuous state space )                |
| ------------------------------------ | --------------------------------- | -------------------------------- |
| Planning (model is available )       |                                   | |
| Learning (learn the model as you go) |                                   |                                  |

chapter 11 of Sutton & Barto covers why interleaving policy evaluations and policy improvement with linear VFA can be unstable
Deadly triad: function approximation; bootstrapping; off-policy learning

**Benefit of Deep Neural Network Approximators**

- Linear value function approximators assume value function is a weighted combination of a set of features, where each feature a function of the state
- Linear VFA often work well given the right set of features, but can require carefully hand designing that feature set
- An alternative is to use a much richer function approximation class that is able to directly go from states without requiring an explicit specification of features
- Local representations including Kernel based approaches have some appealing properties (including convergence results under certain cases) but can’t typically scale well to enormous spaces and datasets
- Alternative: Deep [[courses/xcs224n - natural language processing/3-4 - Neural Networks and Backpropagation|neural networks]]
	- Uses distributed representations instead of local representations
	- Universal function approximator
	- Can potentially need exponentially less nodes/parameters (compared to a shallow net) to represent the same function
	- Can learn the parameters using stochastic gradient descent

## Function Approximation with Cnn

![[courses/xcs234 - reinforcement learning/attachments/xcs234 - reinforcement learning 13.png]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810120350.png]]

**Feature Map**

- All the neurons in the first hidden layer detect exactly the same feature, just at different locations in the input image.
- **Feature**: the kind of input pattern (e.g., a local edge) that makes the neuron produce a certain response level
- Why does this makes sense?
	- Suppose the weights and bias are (learned) such that the hidden neuron can pick out, a vertical edge in a particular local receptive field.
	- That ability is also likely to be useful at other places in the image.
	- Useful to apply the same feature detector everywhere in the image. Yields translation (spatial) invariance (try to detect feature at any part of the image)
	- Inspired by visual system

## Deep Rl - Dqn

Generalization - Using function approximation to help scale up to making decisions in really large domains

Deep [[reinforcement learning]]

- Use deep [[courses/xcs224n - natural language processing/3-4 - Neural Networks and Backpropagation|neural networks]] to represent
	- Value, Q function
	- Policy
	- Model
- Optimize [[loss function]] by stochastic gradient descent (SGD)

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810143147.png]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810143315.png]]
The only difference between SARSA and Q-learning is that SARSA follows a certain policy while Q-learning takes the current max value of the state-action pair as its policy
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810143842.png]]
 **Q-Learning with Value Function Approximation**

 - Q-learning converges to the optimal Q∗ (s, a) using table lookup representation
 - In value function approximation Q-learning we can minimize MSE loss by stochastic gradient descent using a target Q estimate instead of true Q (as we saw with linear VFA)
 - But Q-learning with VFA can diverge
 - Two of the issues causing problems:
	 - Correlations between samples
	 - Non-stationary targets
 - Deep Q-learning (DQN) addresses these challenges by
	 - Experience replay
	 - Fixed Q-targets

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810144515.png]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810144532.png]]

**DQN Pseudocode**
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810144749.png]]
Note there are several hyperparameters and algorithm choices. One needs to choose the neural network architecture, the learning rate, and how often to update the target network. Often a fixed size replay buffer is used for experience replay, which introduces a parameter to control the size, and the need to decide how to populate it

DQN Summary:

- DQN uses experience replay and fixed Q-targets
- Store transition $(s_t , a_t ,r_{t+1},s_{t+1})$ in replay memory D
- Sample random mini-batch of transitions $(s, a, r, s')$ from D
- Compute Q-learning targets w.r.t. old, fixed parameters $w−$
- Optimizes MSE between Q-network and Q-learning targets
- Uses stochastic gradient descent

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810145209.png]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810145513.png]]
Replay is **hugely** important. Why?
	- Because of data efficiency

## Double Dqn

Recall maximization bias challenge: Max of the estimated state-action values can be a biased estimate of the max
Double Q-learning helps solve this problem
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810151315.png]]
Half the time update one Q-function and other half of the time update the other one
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810151722.png]]

## Prioritized Replay

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810164112.png]]
Softmax like prioritization where we compute a probability distribution to sample tuples with based on their priority

### Dueling Dqn

**Value & Advantage Function**

- Intuition: Features needed to accurately represent value may be different than those needed to specify difference in actions
- E.g: Game score may help accurately predict V(s)
	- But not necessarily in indicating relative action values $Q(s, a_1)$ vs $Q(s, a_2)$
- Advantage function (Baird 1993) : $A^{\pi}(s,a)=Q^{\pi}(s,a) - V^{\pi}(s)$

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810165108.png]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810165556.png]]
Advantage function captures how much better a specific action is compared to the average of all the other actions in that state.

### Practical Tips
- Large replay buffers improve robustness of DQN, and memory efficiency is key
	- Use uint8 images, don’t duplicate data
- Be patient. DQN converges slowly—for ATARI it’s often necessary to wait for 10-40M frames (couple of hours to a day of training on GPU) to see results significantly better than random policy
- Try Huber loss on Bellman error
- Consider trying Double DQN—significant improvement from small code change
- Always run at least two different seeds when experimenting
- Learning rate scheduling is beneficial. Try high learning rates in initial exploration period
- To test out your data pre-processing, try your own skills at navigating the environment based on processed frames
- Debug your implementation on a very small toy set

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220810170330.png]]

DNN are very expressive function approximators Can use DNNs to represent the Q function and do MC or TD style methods
