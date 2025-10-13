
> [!resources] Resources
> Contents
> [Autoregressive Models](https://deepgenerativemodels.github.io/notes/autoregressive/), 
> [[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2 - XCS236.pdf]]
[[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2 Slides - XCS236.pdf]]

Technology behind Large Language Models

### FVBSN - Fully Visible Sigmoid Belief Network
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-01-31.png]]
Neural network == Multi layer perceptron
For autoregressive models you need to chose an ordering -> this is easy for language or trajectories since they are essentially time-series. For image pixels its not as obvious

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-01-31-1.png]]

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-01-31-2.png]]
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-01-31-5.png]]
### NADE - Neural Autoregressive Density Estimation
Simple idea where you swap out the logistic regression model from FVBSN with a simple one layer neural network
So each pixel is modeled by doing a lines layer followed by a non linearity of all the pixels that came before it. Then pass this feature vector through one more layer to get a regressed probability value.
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07.png]]
To make it a bit more parameter efficient have one giant weight matrix A and then reuse slices of it as you go along. This also makes the computation a lot faster because the forward pass of the previous pixels can be cached and just need to do it for the current pixel
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-1.png]]

Can be generalized to a categorical distribution that is sampling color images with pixel values between 0 & 255. Just swap out the last regression layer with a categorical layer and then run softmax on it to get a clean one probability like output
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-2.png]]
To get continuous random variables the output can be modeled as a continuous distribution, for example: mixture of gaussians. The just get a set of means and variances from the network representing that continuous distribution
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-3.png]]

### Autoregressive models vs Autoencoders
Autoencoders take the input map it into a latent space and then remap it back to the output space. You use some form of reconstruction loss function.
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-4.png]]
By forcing an ordering to an autoencoder you get back an autoregressive model
You can mask out parts of an autoencoder to make it an autoregressive model -> MADE: Masked Autoencoder for Distribution Estimation
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-6.png]]

Use RNNs. which a recursive computation that maintains a history vector (in some latent space) and you update the history vector as you step through the ordering in your input
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-7.png]]
Pros:
- Can be applied to sequences of arbitrary length.
- Very general: For every computable function, there exists a finiteRNN that can compute it
Cons:
- Still requires an ordering
- Sequential likelihood evaluation (very slow for training)
- Sequential generation (unavoidable in an autoregressive model)
Issues with RNNs and why they are not used in SoTA language models
- one hidden vector needs to capture & summarize  all the context & history. For example,h(4)needs to summarize the meaning of “My friendopened the”.
- Sequential evaluations: cannot be parallelized so not great with GPUs (at training time)
- Exploding/vanishing gradients when accessing information from manysteps back

### Attention based Models vs RNNs

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-8.png]]

Current state of the art (GPTs): replace RNN with Transformer
- Attention mechanisms to adaptively focus only on relevant context
- Avoid recursive computation. Use only self-attention to enable parallelization
- Needsmaskedself-attention to preserve autoregressive structure
- Demo:https://transformer.huggingface.co/doc/gpt2-large
- Demo:https://huggingface.co/spaces/huggingface-projects/llama-2-13b-chat

**Back to RNNs**
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-9.png]]
Convolutional architectures work much better on images
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-10.png]]
You can use masked attention on images as well with Transformer like models - though they are computationally expensive
The **inductive bias** (also known as **learning bias**) of a [learning algorithm](https://en.wikipedia.org/wiki/Machine_learning "Machine learning") is the set of assumptions that the learner uses to predict outputs of given inputs that it has not encountered.

RNNs can be much more efficient at inference time

One application of these models is to prevent Adversarial Attacks and for Anomaly Detection
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-11.png]]
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-12.png]]

### KL Divergence
Measures the expected number of extra bits required to describe samples from p(x) using a compression code based on q instead of p

KL divergence is one way of measuring closeness. It is an assymetric measure and always greater than 0

Learning as density estimation
- We want to learn the full distribution so that later we can answer any probabilistic inference query
- In this setting we can view the learning problem as density estimation
- We want to construct P_θ as ”close” as possible to P_data (recall we assume we are given a dataset D of samples from P_data)
- How do we evaluate ”closeness”?
- KL-divergence is one possibility
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-17.png]]
- It measures the ”compression loss” (in bits) of using P_θ instead of P_data


### Monte Carlo Estimation

Basically you can never know true data distribution so just computing the expected value based on the dataset you have can serve as a meaningful estimate. (1/T)\*g(t) where g(t) is a sample from the dataset

Check out the slides: covers Maximum Likelihood Estimation Learning and Stochastic Gradient Descent -> a bunch of math 

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-15.png]]
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-16.png]]

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-13.png]]
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Autoregressive Models - Module 2-2025-02-07-14.png]]
