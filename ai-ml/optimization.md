---
created: 2023-05-01-Monday 14:30
modified: 2023-05-02-Tuesday 11:57
publish: 
---

> [!NOTE] Iterative Refinement
> When we start with a random set of weights and refine them step by step until the loss is minimized.

# [CS231n - Optimization: Stochastic Gradient Descent](https://cs231n.github.io/optimization-1/)

## Gradients

As a technical note, you can also see that the *kinks* in the Hinge [[loss function]] (due to the max operation) technically make the loss function non-differentiable because at these kinks the gradient is not defined. However, the [subgradient](http://en.wikipedia.org/wiki/Subderivative) still exists and is commonly used instead.

In one-dimensional functions, the slope is the instantaneous rate of change of the function at any point you might be interested in. The gradient is a generalization of slope for functions that don’t take a single number but a vector of numbers. Additionally, the gradient is just a vector of slopes (more commonly referred to as **derivatives**) for each dimension in the input space. The mathematical expression for the derivative of a 1-D function with respect its input is:

$\frac{df(x)}{dx} = \lim_{h \to 0}\frac{f(x+h)-f(x)}{h}$

> [!TIP] Use this formula for computing finite differences
> $\frac{df(x)}{dx} = \lim_{h \to 0}\frac{f(x+h)-f(x-h)}{2h}$
> has error terms on order of $O(h^2)$ (i.e. it is a second order approximation)

When the functions of interest take a vector of numbers instead of a single number, we call the derivatives **partial derivatives**, and the gradient is simply the vector of partial derivatives in each dimension.

The gradient tells us the direction in which the function has the steepest rate of increase, but it does not tell us how far along this direction we should step. Choosing the step size (also called the *learning rate*) will become one of the most important (and most headache-inducing) hyperparameter settings in training a neural network.

**Numerical Gradient - Finite Differences**
Pick a very small $h$ such as $1e-5$ and compute the finite difference according to the formula above.
Evaluating the numerical gradient has complexity linear in the number of parameters. In our example we had 30730 parameters in total and therefore had to perform 30,731 evaluations of the loss function to evaluate the gradient and to perform only a single parameter update. This problem only gets worse, since modern Neural Networks can easily have tens of millions of parameters. Clearly, this strategy is not scalable and we need something better.

**Analytical Gradient - Calculus**
Once you derive the expression (no approximations) for the gradient it is straight-forward to implement the expressions and use them to perform the gradient update (very fast).

## Gradient Descent

```python
# Vanilla Gradient Descent

while True:
  weights_grad = evaluate_gradient(loss_fun, data, weights)
  weights += - step_size * weights_grad # perform parameter update
```

### Mini-batch Gradient Descent

In large-scale applications (such as the ILSVRC challenge), the training data can have on order of millions of examples. Hence, it seems wasteful to compute the full loss function over the entire training set in order to perform only a single parameter update. A very common approach to addressing this challenge is to compute the gradient over **batches** of the training data. For example, in current state of the art ConvNets, a typical batch contains 256 examples from the entire training set of 1.2 million. This batch is then used to perform a parameter update:

```python
# Vanilla Minibatch Gradient Descent

while True:
  data_batch = sample_training_data(data, 256) # sample 256 examples
  weights_grad = evaluate_gradient(loss_fun, data_batch, weights)
  weights += - step_size * weights_grad # perform parameter update
```

Gradient from a mini-batch is a good approximation of the gradient of the full objective. Therefore, much faster convergence can be achieved in practice by evaluating the mini-batch gradients to perform more frequent parameter updates.

The size of the mini-batch is a hyperparameter but it is not very common to cross-validate it. It is usually based on memory constraints (if any), or set to some value, e.g. 32, 64 or 128. We use powers of 2 in practice because many vectorized operation implementations work faster when their inputs are sized in powers of 2.

### Stochastic Gradient Descent

Extreme case of [[#Mini-batch gradient descent]] where the mini-batch contains only a single example.
This is relatively less common to see because in practice due to vectorized code optimizations it can be computationally much more efficient to evaluate the gradient for 100 examples, than the gradient for one example 100 times. Even though SGD technically refers to using a single example at a time to evaluate the gradient, it is commonly used to refer to minibatch or batch gradient descent.

## Optimization Techniques

### Vanilla Update
```
# Vanilla update
x += - learning_rate * dx
```

where `learning_rate` is a hyperparameter - a fixed constant

### Momentum Update
```
# Momentum update
v = mu * v - learning_rate * dx # integrate velocity
x += v # integrate position
```

`v` is initialized to 0 and `mu` is the momentum hyperparameter that acts as a dampener.
When cross-validated, this parameter is usually set to values such as [0.5, 0.9, 0.95, 0.99]

### Nesterov Momentum

Slightly different version of the momentum update that has recently been gaining popularity. It enjoys stronger theoretical converge guarantees for convex functions and in practice it also consistenly works slightly better than standard momentum.

### Annealing - Learning Rate

In training deep networks, it is usually helpful to anneal the learning rate over time. Good intuition to have in mind is that with a high learning rate, the system contains too much kinetic energy and the parameter vector bounces around chaotically, unable to settle down into deeper, but narrower parts of the loss function.

### Second order Methods

based on [Newton’s method](http://en.wikipedia.org/wiki/Newton%27s_method_in_optimization), which iterates the following update:

$x←x−[Hf(x)]^{−1}∇f(x)$
Here, $Hf(x)$ is the [Hessian matrix](http://en.wikipedia.org/wiki/Hessian_matrix), which is a square matrix of second-order partial derivatives of the function. The term $∇f(x)$ is the gradient vector, as seen in Gradient Descent. Intuitively, the Hessian describes the local curvature of the loss function, which allows us to perform a more efficient update. In particular, multiplying by the inverse Hessian leads the optimization to take more aggressive steps in directions of shallow curvature and shorter steps in directions of steep curvature. Note, crucially, the absence of any learning rate hyperparameters in the update formula, which the proponents of these methods cite this as a large advantage over first-order methods.
Several methods approximate the Hessian matrix - most popular is [L-BFGS](http://en.wikipedia.org/wiki/Limited-memory_BFGS)

**Not very common to use for large deep neural nets. SGD is prefered because it is much simpler and scales well.**

### Per-parameter Adaptive Learning Rate Methods

Tuning the learning rates is an expensive process, so much work has gone into devising methods that can adaptively tune the learning rates, and even do so per parameter.

#### Adagrad
#### Rmsprop

RMSProp update adjusts the Adagrad method in a very simple way in an attempt to reduce its aggressive, monotonically decreasing learning rate - [slide 29 of Lecture 6](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf) of Geoff Hinton’s Coursera class

#### Adam

Looks a bit like RMSProp with momentum

![[optimization-2023-05-02.gif|400]] ![[optimization-2023-05-02-1.gif|400]]

# Stanford Bootcamp
![[inpaint.ipynb]]

![[nonneg_matrix_fact.ipynb]]

![[quadratic_minimization.ipynb]]

![[polynomial-fit.ipynb]]

![[least-squares.ipynb]]

![[robust_kalman.ipynb]]

![[smooth.ipynb]]

![[set_examples.ipynb]]

![[portfolio_optimization.ipynb]]

![[optimal_advertising.ipynb]]

![[huber.ipynb]]

![[lasso.ipynb]]