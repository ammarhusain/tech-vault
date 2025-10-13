---
created: 2022-09-05-Monday 23:32
modified: 2023-03-10-Friday 23:15
---

![500](courses/cs285%20-%20deeprl/attachments/image37.png)![500](courses/cs285%20-%20deeprl/attachments/image57.png)

To run Tensorboard if it complains (command not found)

python3 -m tensorboard.main --logdir=.

![500](courses/cs285%20-%20deeprl/attachments/image58.png)

![500](courses/cs285%20-%20deeprl/attachments/image12.png)![500](courses/cs285%20-%20deeprl/attachments/image2.png)![500](courses/cs285%20-%20deeprl/attachments/image31.png)![500](courses/cs285%20-%20deeprl/attachments/image49.png)

Q Function: How good is this state action pair? What is the reward if I take this action in this particular state?

Value Function: How good is this state over all of my available actions? Q-func is conditioned on action while Value-func is not. Value-func is the expectation of the Q-value.

![500](courses/cs285%20-%20deeprl/attachments/image9.png)![500](courses/cs285%20-%20deeprl/attachments/image48.png)![500](courses/cs285%20-%20deeprl/attachments/image25.png)![500](courses/cs285%20-%20deeprl/attachments/image22.png)![500](courses/cs285%20-%20deeprl/attachments/image15.png)![500](courses/cs285%20-%20deeprl/attachments/image26.png)

![500](courses/cs285%20-%20deeprl/attachments/image52.png)

![500](courses/cs285%20-%20deeprl/attachments/image4.png)

![500](courses/cs285%20-%20deeprl/attachments/image1.png)

HW - 2

Problem#4: Ideal batch size ~ 1000-10000 samples with learning rate: 0.01

Problem#7: Best configuration:  *b50000_lr.02* aka batchsize 50k, learning rate 0.02

 Problem 7 deliverables: Reward to go performs a lot better … Baseline brings down the eval return a bit thats probably because it helps reduce the variance.

Subtracting baselines just tries to promote rewards that are above average from the rest. This helps when absolute reward values might be large for both good & bad samples.

# Lecture 6: Actor Critic Algorithms (9/18/19)

Advantage is usually Q(s,a) - V(s) which essentially means how much better is this action compared with the other actions in this state.

Baseline (aka quantity that is subtracted from Q value) to reduce variance, can be either state dependent as in V(s) above for the Advantage or state independent which would average rewards over all possible states. I think state dependent baselines (such as V(s)) are better.

Discount factors: Handle the problem when the target values you’re trying to fit won’t constantly increase at every time step. It adds a notion of time to the stationary value function approximator. This is equivalent to adding a death state to the MDP that you can reach from any state in every transition with probability (1-gamma). Gamma helps you reduce variance in your V estimate.

![500](courses/cs285%20-%20deeprl/attachments/image21.png)![500](courses/cs285%20-%20deeprl/attachments/image19.png)

- IF you update with tiny batches then you will have very high variance in your gradient updates. More samples means variance gets reduced.
- You could use Q function (state & action dependent) as baseline to subtract, rather than the Value function (state dependent). Though this is not correct but can be made to work with some tricks.
- Generalized advantage estimation is when you don’t want to cut off the sum of rewards at a certain ‘n’ and then pick the value function estimator moving forward. Rather have a more soft cutoff.
- Approximate dynamic programming, value function methods, fitted Q algorithms all kind of mean the same thing … Fit Value (or advantage or Q) func and then policy is simply argmax action.
- For fully observed MDPs there is always a deterministic policy that will be optimal (though there could also be a stochastic one: such as when 2 nodes have equal Q values pick either one randomly). This is not true for POMDPs.
- Value iteration is very simply the recursive updating of a giant state by action table where you recursively refine the Q(s,a) values until they converge. The policy then is to just use the argmax from each row (aka state).

![500](courses/cs285%20-%20deeprl/attachments/image35.png)![500](courses/cs285%20-%20deeprl/attachments/image53.png)

![500](courses/cs285%20-%20deeprl/attachments/image36.png)![500](courses/cs285%20-%20deeprl/attachments/image8.png)![500](courses/cs285%20-%20deeprl/attachments/image51.png)

- Deep Q learning is not gradient descent. Even in the tabular case, it is a fixed point iteration.

# Lecture 10: Model Based Planning

![500](courses/cs285%20-%20deeprl/attachments/image29.png)![500](courses/cs285%20-%20deeprl/attachments/image41.png)

- Transition dynamics are knowing P(s_t+1 | s_t, a_t).
- This lecture didn’t contain any learning. Only strategies to chose actions under perfect knowledge of system dynamics: Optimal control, trajectory optimization, planning.
- Cross entropy method is extremely simple & parallelizable. But suffers with dimensionality (<~50). Only open loop planning since all actions are a priori collected.
- Monte Carlo tree search is basically pick a node by some score function and then use some “default” policy to further explore within that node. As you explore more, you can refine the “default” policy to get better/smarter.

![500](courses/cs285%20-%20deeprl/attachments/image16.png)![500](courses/cs285%20-%20deeprl/attachments/image59.png)![500](courses/cs285%20-%20deeprl/attachments/image46.png)![500](courses/cs285%20-%20deeprl/attachments/image33.png)

![500](courses/cs285%20-%20deeprl/attachments/image24.png)![500](courses/cs285%20-%20deeprl/attachments/image28.png)

- Basic Idea for LQR: Since u_t is fully determined by x_t we can eliminate it via substitution. Then we solve for u_t-1 in terms of x_t-1 but u_t-1 also affects x_t … So do a bunch of complex linear algebra manipulations to keep doing these substitutions up until we reach x_0 which is what we know.
- In simple words we figure out the last best action to get to the target state. Then we go back in time (backward recursion) to frame the equation with respect to our current state. Then for the forward pass we simply walk out and solve for all the actions from 0 to T.
- Assumes linear system dynamics, kind of like Kalman Filter, and a quadratic cost function that we try to optimize. Does this perhaps mean we are trying to minimize RMSE?
- (side note) Matrix inversion is cubic in complexity but can be done very efficiently through blas libraries.

![500](courses/cs285%20-%20deeprl/attachments/image14.png)![500](courses/cs285%20-%20deeprl/attachments/image27.png)

- The Q and V values in the equation have basically the same meaning as before (from Q-learning / value functions).
- For cases with nonlinear systems, use iterative LQR (aka differential dynamic programming): take the first derivative of the dynamics (linearize it) and second derivative of the cost (quadratize it) [Taylor series expansion]
- iLQR is quite similar to Newton's method.
- LQR based methods are local policies as in they optimize over a relatively short planning horizon rather than the entire episode.

![500](courses/cs285%20-%20deeprl/attachments/image17.png)![500](courses/cs285%20-%20deeprl/attachments/image11.png)

# Lecture 11: Model Based Reinforcement Learning

# ![500](courses/cs285%20-%20deeprl/attachments/image47.png)![500](courses/cs285%20-%20deeprl/attachments/image18.png)
- Model based RL 0.5 : Essentially how system identification works in classical robotics. Particularly effective if we can hand engineer a dynamics representation using physics & fit just a few parameters. (As in the model is not a full black box like a NN). Some care should be taken to design a good base policy since that's how we sample/explore the space.

![500](courses/cs285%20-%20deeprl/attachments/image20.png)![500](courses/cs285%20-%20deeprl/attachments/image40.png)

Model based RL v1.0 is very similar to DAGGER (from imitation learning). We execute policy, collect more data and relabel it as expert data.

Problem with model learning is that it is easy to overfit the data. So we need some way of adding uncertainty.

Only take actions for which we think we’ll get high reward in expectation (w.r.t uncertain dynamics). This avoids “exploiting” the model.

![500](courses/cs285%20-%20deeprl/attachments/image39.png)![500](courses/cs285%20-%20deeprl/attachments/image6.png)

There are two types of uncertainties and they are not the same.

![500](courses/cs285%20-%20deeprl/attachments/image43.png)

For Idea#2 we are trying to estimate a distribution of parameters that can all fit the data. I.e we are trying to find a set of different NNs with different weights that all perform roughly equal for this dataset. Then we can use their consensus to estimate uncertainty.

One way could be using Bayesian NNs, where you’re estimating a distribution for each neuron weight rather than a real value.

Bootstrap ensembles are very simply just multiple NNs randomly initialized (differently). Its a very crude approximation because # of models is usually small (<10).

![500](courses/cs285%20-%20deeprl/attachments/image32.png)![500](courses/cs285%20-%20deeprl/attachments/image13.png)![500](courses/cs285%20-%20deeprl/attachments/image42.png)![500](courses/cs285%20-%20deeprl/attachments/image42.png)

o_t is the image that we observe and s_t is some underlying state such as paddle position. Assumption is that s_t is low dimensional and partially observable through o_t.

With latent space models we are trying to learn three models: observation (what should my image look like given my gripper position), dynamics (how does my action affect how my gripper moves), reward (how much reward can I expect to get given my latent state and planned action).

![500](courses/cs285%20-%20deeprl/attachments/image7.png)![500](courses/cs285%20-%20deeprl/attachments/image23.png)

For the full smoothing posterior “encoder”, we would feed in all the images we’ve seen & actions taken into an RNN to encode a hidden state over time.

Single-step encoder is quite simply some ConvNet that produces an embedding. g_psi is the encoding/embedding.

![500](courses/cs285%20-%20deeprl/attachments/image5.png)![500](courses/cs285%20-%20deeprl/attachments/image56.png)

Learning directly in observation space is basically like hallucinating what the next should look like and what action will make that hallucination come alive. It's pretty much what you saw at RSS 2019.

![500](courses/cs285%20-%20deeprl/attachments/image54.png)

# Lecture 11: Model Based Reinforcement Learning

For Policy gradient methods, we don't have to do backpropagation through time (BPTT) because we are differentiating an expectation. I.e. We don't have to compute derivative of every state wrt action in time because we just compute derivatives of the probabilities of all the samples rather than the actual dynamics f(s_t+1|s_t,a_t).

Policy gradient pays high price because it has very high variance, while [[courses/xcs224n - natural language processing/3-4 - Neural Networks and Backpropagation|backprop]] a policy with model has low variance but suffers from vanishing/exploding gradients.

![500](courses/cs285%20-%20deeprl/attachments/image30.png)![500](courses/cs285%20-%20deeprl/attachments/image55.png)

Its hard to say when it is a good idea to learn just a Q function and when to learn a model as well, because a Q function is essentially a model of expected reward. In some cases, such as image (states), learning a model is weird because you’re trying to predict/hallucinate the next image given current image & action. This is currently not well understood within DRL on when to use a model and when not.

The basic idea here is that the model is just acting like a mini simulator to do short rollouts while the focus is still to learn a Q function (and policy function for Actor Critic). Though its actually also learning a dynamics model (and maybe rewards function).

![500](courses/cs285%20-%20deeprl/attachments/image34.png)![500](courses/cs285%20-%20deeprl/attachments/image3.png)![500](courses/cs285%20-%20deeprl/attachments/image38.png)

# Lecture 12: Variational Inference and Generative Models

Mixture density networks: NNs that output mean & variance for a bunch of gaussians. GMMs through NNs.

[[courses/xcs224n - natural language processing/3-4 - Neural Networks and Backpropagation|Neural nets]] can be thought of as basically highly non linear functions that map a normal distribution with mean 0 and variance 1 of some input dim d to some arbitrary output distribution of dimension o.

![500](courses/cs285%20-%20deeprl/attachments/image44.png)![500](courses/cs285%20-%20deeprl/attachments/image10.png)![500](courses/cs285%20-%20deeprl/attachments/image50.png)![500](courses/cs285%20-%20deeprl/attachments/image45.png)

z in the cases above is the latent state. So we are trying to learn P(x|z) where x is the observed state, like images and z is some underlying latent state. Notation is a bit confusing because we were using o (observed) & x/s (actual state that may be latent) before.

For imitation learning we were feeding in an image (state or x) and adding (or concatenating?) random noise from a unit normal distribution to feed into a DNN to get a multi modal policy conditioned on latent variable. We were hoping that that random noise somehow magically gets converted to a latent representation.
