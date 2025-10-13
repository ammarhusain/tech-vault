---
created: 2023-05-01-Monday 15:23
modified: 2023-05-30-Tuesday 14:06
publish: 
---

# Sandbox

[[numpy-minimal_net.ipynb]]
[[neural-network-toy.ipynb]]

# [CS231n - Neural Nets Primer](https://cs231n.github.io/neural-networks-1/)

[Article](https://cs231n.github.io/neural-networks-case-study/)

Having a non-linearity (aka activation function) after every linear layer is critical computationally - if we left it out, the two matrices could be collapsed to a single matrix and therefore the predicted class scores would again be a linear function of the input. The non-linearity is where we get the *wiggle*. The parameters are learned with stochastic gradient descent, and their gradients are derived with chain rule ([[backpropagation]]).
A very basic three-layer neural network could analogously look like $s=W_3\max(0, W_2 \max(0, W_1x))$

> [!NOTE] A single neuron can be used to implement a binary [[linear classification|linear classifier]] (e.g. binary Softmax or binary SVM classifiers)

## Activation Functions

Every activation function (or *non-linearity*) takes a single number and performs a certain fixed mathematical operation on it. There are several activation functions you may encounter in practice:

### Sigmoid

$\sigma(x)=1/(1+e^{-x})$
t takes a real-valued number and “squashes” it into range between 0 and 1. In particular, large negative numbers become 0 and large positive numbers become 1.
In practice, the sigmoid non-linearity has recently fallen out of favor and it is rarely ever used. It has two major drawbacks:

- Sigmoids saturate and kill gradients:
	Pay extra caution when initialising the weights of sigmoid neurons to prevent saturation. For example, if the initial weights are too large then most neurons would become saturated.
	If the local gradient is very small, it will effectively “kill” the gradient and almost no signal will flow through the neuron to its weights and recursively to its data

- Sigmoid outputs are not zero-centered

### Tanh

Squashes a real-valued number to the range [-1, 1].
Like the sigmoid neuron, its activations saturate, but unlike the sigmoid neuron its output is zero-centered. Therefore, in practice the *tanh non-linearity is always preferred to the sigmoid nonlinearity.*
tanh neuron is simply a scaled sigmoid neuron - $\tanh(x) = 2\sigma(2x) - 1$

### ReLU

$f(x) = \max(0,x)$
Activation is simply thresholded at 0.
**Pros:**

- Found to greatly accelerate the convergence of stochastic gradient descent compared to sigmoid/tanh functions. It is argued that this is due to its. linear, non-saturating form.
- Compared to tanh/sigmoid that involve expensive operations (exponentials etc), ReLU can be implemented by simple thresholding.
**Cons:**
- ReLU units can be fragile during training and can “die”. For example, a large gradient flowing through a ReLU neuron could cause the weights to update in such a way that the neuron will never activate on any datapoint again. The ReLU units can irreversibly die during training since they can get knocked off the data manifold.

### Leaky ReLU

$f(x) = \mathbb{1}(x<0)(\alpha x) + \mathbb{1}( x >=0)(x)$ where $\alpha$ is a small constant.
Leaky ReLUs are one attempt to fix the “dying ReLU” problem. Instead of the function being zero when x < 0, a leaky ReLU will instead have a small positive slope

### Maxout

Computes the function : $\max(w_1^Tx + b_1, w_2^Tx + b_2)$
Notice that both ReLU and Leaky ReLU are a special case of this form - for example, for ReLU we have $w1,b1=0$
The Maxout neuron therefore enjoys all the benefits of a ReLU unit (linear regime of operation, no saturation) and does not have its drawbacks (dying ReLU). However, unlike the ReLU neurons it doubles the number of parameters for every single neuron, leading to a high total number of parameters.

> [!NOTE] it is very rare to mix and match different types of neurons in the same network, even though there is no fundamental problem with doing so.

> [!NOTE] “*What neuron type should I use?*”
> Use the ReLU non-linearity, be careful with your learning rates and possibly monitor the fraction of “dead” units in a network. If this concerns you, give Leaky ReLU or Maxout a try. Never use sigmoid. Try tanh, but expect it to work worse than ReLU/Maxout.

## Architectures
- Neural Networks are modeled as collections of neurons that are connected in an acyclic graph.
- Instead of an amorphous blobs of connected neurons, Neural Network models are often organized into distinct layers of neurons. For regular neural networks, the most common layer type is the **fully-connected layer** in which neurons between two adjacent layers are fully pairwise connected, but neurons within a single layer share no connections.
- Can also be referred to as ***"Artificial Neural Networks (ANN)"*** or ***"Multi-layer Perceptrons (MLP)"***
- Unlike all layers in a Neural Network, the output layer neurons most commonly do not have an activation function.

> [!NOTE] Why layers?
> One of the primary reasons that Neural Networks are organized into layers is that this structure makes it very simple and efficient to evaluate Neural Networks using matrix vector operations.

The forward pass of a fully-connected layer corresponds to one matrix multiplication followed by a bias offset and an activation function.

```python
# forward-pass of a 3-layer neural network:
f = lambda x: 1.0/(1.0 + np.exp(-x)) # activation function (use sigmoid)
x = np.random.randn(3, 1) # random input vector of three numbers (3x1)
h1 = f(np.dot(W1, x) + b1) # calculate first hidden layer activations (4x1)
h2 = f(np.dot(W2, h1) + b2) # calculate second hidden layer activations (4x1)
out = np.dot(W3, h2) + b3 # output neuron (1x1)
```

> [!NOTE] Neural Networks with at least one hidden layer are *universal approximators*

The fact that deeper networks (with multiple hidden layers) can work better than a single-hidden-layer networks is an empirical observation, despite the fact that their representational power is equal.

> [!Tip]
> It is often the case that 3-layer neural networks will outperform 2-layer nets, but going even deeper (4,5,6-layer) rarely helps much more. This is in stark contrast to Convolutional Networks, where depth has been found to be an extremely important component for a good recognition system (e.g. on order of 10 learnable layers).

As we increase the size and number of layers in a Neural Network, the **capacity** of the network increases => more representational power.

**Overfitting** occurs when a model with high capacity fits the noise in the data instead of the (assumed) underlying relationship. For example, the model with 20 hidden neurons fits all the training data but at the cost of segmenting the space into many disjoint decision regions.

In practice, it is always better to use other preferred methods (such as L2 regularisation, dropout, input noise) to control overfitting instead of the number of neurons. The subtle reason behind this is that smaller networks are harder to train with local methods such as Gradient Descent.

## Weight Initialization

> [!WARNING] **All zero initialization**
> if every neuron in the network computes the same output, then they will also all compute the same gradients during backpropagation and undergo the exact same parameter updates. In other words, there is no source of asymmetry between neurons if their weights are initialized to be the same.

### Small Random Numbers

it is common to initialize the weights of the neurons to small numbers and refer to doing so as *symmetry breaking*. The idea is that the neurons are all random and unique in the beginning, so they will compute distinct updates and integrate themselves as diverse parts of the full network. The implementation for one weight matrix might look like `W = 0.01* np.random.randn(D,H)`, where `randn` samples from a zero mean, unit standard deviation gaussian.

### Calibrating the Variances with 1/sqrt(n)

One problem with the above suggestion is that the distribution of the outputs from a randomly initialized neuron has a variance that grows with the number of inputs. It turns out that we can normalize the variance of each neuron’s output to 1 by scaling its weight vector by the square root of its *fan-in* (i.e. its number of inputs).
That is, the recommended heuristic is to initialize each neuron’s weight vector as: `w = np.random.randn(n) / sqrt(n)`, where `n` is the number of its inputs. This ensures that all neurons in the network initially have approximately the same output distribution and empirically improves the rate of convergence.

> [!TIP] neural networks with ReLU neurons
> the initialization `w = np.random.randn(n) * sqrt(2.0/n)`, and is the current recommendation for use in practice in this specific case

### Initializing Biases

For ReLU non-linearities, some people like to use small constant value such as 0.01 for all biases because this ensures that all ReLU units fire in the beginning and therefore obtain and propagate some gradient. However, it is not clear if this provides a consistent improvement (in fact some results seem to indicate that this performs worse) and ====it is more common to simply use 0 bias initialization====.

### Batch Normalization

[Batch Normalization](http://arxiv.org/abs/1502.03167) alleviates a lot of headaches with properly initializing neural networks by explicitly forcing the activations throughout a network to take on a unit gaussian distribution at the beginning of the training.

> [!TIP]
> networks that use Batch Normalization are significantly more robust to bad initialization

Can be interpreted as doing preprocessing at every layer of the network, but integrated into the network itself in a differentiable manner. Neat!
