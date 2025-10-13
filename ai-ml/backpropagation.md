**Related:**
[[courses/xcs224n - natural language processing/3-4 - Neural Networks and Backpropagation]]


# [CS231n notes on backprop](http://cs231n.github.io/optimization-2/)

- The primary reason we are interested in this problem is that in the specific case of neural networks, f will correspond to the loss function ( L ) and the inputs x will consist of the training data and the neural network weights.
- Note that (as is usually the case in Machine Learning) we think of the training data as given and fixed, and of the weights and biases W,b as variables we have control over.
![[backpropagation-2023-04-28.png|600]]
- Derivative on each variable tells you the sensitivity of the whole expression on its value.
- The gradient $∇f$ is the vector of partial derivatives, so we have that $∇f=[∂f∂x,∂f∂y]$. Even though the gradient is technically a vector, we will often use terms such as _“the gradient on x”_ instead of the technically correct phrase _“the partial derivative on x”_ for simplicity.
![[backpropagation-2023-04-28-1.png|700]]
- Backpropagation is a beautifully local process. Every gate in a circuit diagram gets some inputs and can right away compute two things: 1. its output value and 2. the _local_ gradient of its output with respect to its inputs. Notice that the gates can do this completely independently without being aware of any of the details of the full circuit that they are embedded in. 
- Once the forward pass is over, during backpropagation the gate will eventually learn about the gradient of its output value on the final output of the entire circuit. Chain rule says that the gate should take that gradient and multiply it into every gradient it normally computes for all of its inputs.
- During the backward pass in which the chain rule is applied recursively backwards through the circuit, the add gate (which is an input to the multiply gate) learns that the gradient for its output was -4. To continue the recurrence and to chain the gradient, the add gate takes that gradient and multiplies it to all of the local gradients for its inputs (making the gradient on both **x** and **y** 1 * -4 = -4). 
- Notice that this has the desired effect: If **x,y** were to decrease (responding to their negative gradient) then the add gate’s output would decrease, which in turn makes the multiply gate’s output increase.
- Backpropagation can thus be thought of as gates communicating to each other (through the gradient signal) whether they want their outputs to increase or decrease (and how strongly), so as to make the final output value higher.

![[backpropagation-2023-04-28-2.png|800]]
- In practice it is always helpful to break down the forward pass into stages that are easily backpropped through. 
- The details of how the backpropagation is performed, and which parts of the forward function we think of as gates, is a matter of convenience. It helps to be aware of which parts of the expression have easy local gradients, so that they can be chained together with the least amount of code and effort.

Lets see this with another example. Suppose that we have a function of the form:

$f(x,y)=\frac{x+\sigma(y)}{\sigma(x) + (x+y)^2}$
![[backpropagation-2023-04-28-3.png|750]]
- By the end of the expression we have computed the forward pass. Notice that we have structured the code in such way that it contains multiple intermediate variables, each of which are only simple expressions for which we already know the local gradients. Therefore, computing the backprop pass is easy: We’ll go backwards and for every variable along the way in the forward pass (`sigy, num, sigx, xpy, xpysqr, den, invden`) we will have the same variable, but one that begins with a `d`, which will hold the gradient of the output of the circuit with respect to that variable. 
- Additionally, note that every single piece in our backprop will involve computing the local gradient of that expression, and chaining it with the gradient on that expression with a multiplication. For each row, we also highlight which part of the forward pass it refers to:
![[backpropagation-2023-04-28-4.png|800]]
The forward expression involves the variables **x,y** multiple times, so when we perform backpropagation we must be careful to use += instead of = to accumulate the gradient on these variables (otherwise we would overwrite it). This follows the _multivariable chain rule_ in Calculus, which states that if a variable branches out to different parts of the circuit, then the gradients that flow back to it will add.

Three most commonly used gates in neural networks (_add,mul,max_), all have very simple interpretations in terms of how they act during backpropagation. Consider this example circuit:

![[backpropagation-2023-04-28-5.png|700]]
- Notice that if one of the inputs to the multiply gate is very small and the other is very big, then the multiply gate will do something slightly unintuitive: it will assign a relatively huge gradient to the small input and a tiny gradient to the large input. Note that in linear classifiers where the weights are dot producted $w^Tx_i$ (multiplied) with the inputs, this implies that the scale of the data has an effect on the magnitude of the gradient for the weights. For example, if you multiplied all input data examples $x_i$ by 1000 during preprocessing, then the gradient on the weights will be 1000 times larger, and you’d have to lower the learning rate by that factor to compensate. This is why preprocessing matters a lot!
	- This is why data is normalized to be between 0 and 1 across batches/data points as well as across the feature dimensions of a single data point. 
**staged computation**: You always want to break up your function into modules for which you can easily derive local gradients, and then chain them with chain rule. Crucially, you almost never want to write out these expressions on paper and differentiate them symbolically in full, because you never need an explicit mathematical equation for the gradient of the input variables. Hence, decompose your expressions into stages such that you can differentiate every stage independently