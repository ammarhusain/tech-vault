---
created: 2022-09-08-Thursday 11:21
modified: 2023-05-06-Saturday 12:41
---

loss is the objective function to minimize. In neural networks, the optimization is done with gradient descent and backpropagation.
[[metrics]] such as accuracy are much more useful for humans to understand the performance of a neural network even though they might not be good choices for loss functions since they might not be differentiable.

[[cross_entropy_2d.py]]

# Miscellaneous
[[2023-05-30-Tuesday]] Randomly encountered loss functions:
- Contrastive Loss - used in CLIP to tie images with text (multi-modal)
- Focal Loss - used in RetinaNet

# [How to Choose Loss Functions When Training Deep Learning Neural Networks](https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/)
## Regression Loss Functions
### Mean Squared Error Loss (default)

Calculated as the average of the squared differences between the predicted and actual values. The result is always positive regardless of the sign of the predicted and actual values and a perfect value is 0.0. The squaring means that larger mistakes result in more error than smaller mistakes, meaning that the model is punished for making larger mistakes.

### Mean Squared Logarithmic Error Loss

Regression problems in which the target value has a spread of values and when predicting a large value, you may not want to punish a model as heavily as mean squared error.
It has the effect of relaxing the punishing effect of large differences in large predicted values.

### Mean Absolute Error Loss

More robust to outliers

## Binary Classification Loss Functions
### Binary Cross-entropy (default)

Preferred loss function under the inference framework of maximum likelihood. It is the loss function to be evaluated first and only changed if you have a good reason.
Cross-entropy will calculate a score that summarizes the average difference between the actual and predicted probability distributions for predicting class 1. The score is minimized and a perfect cross-entropy value is 0.

### Hinge Loss

Primarily developed for use with Support Vector Machine (SVM) models.

### Squared Hinge Loss

A popular extension is called the squared hinge loss that simply calculates the square of the score hinge loss. It has the effect of smoothing the surface of the error function and making it numerically easier to work with.

If using a hinge loss does result in better performance on a given binary classification problem, is likely that a squared hinge loss may be appropriate.


## Multi-Class Classification Loss Functions
Predictive modeling problems where examples are assigned one of more than two classes.
### Multi-Class Cross-Entropy Loss (default)
preferred loss function under the inference framework of maximum likelihood. It is the loss function to be evaluated first and only changed if you have a good reason.
Cross-entropy will calculate a score that summarizes the average difference between the actual and predicted probability distributions for all classes in the problem. The score is minimized and a perfect cross-entropy value is 0.

### Sparse Multiclass Cross-Entropy Loss
A possible cause of frustration when using cross-entropy with classification problems with a large number of labels is the one hot encoding process (such as thousands of words in vocabulary)
Sparse cross-entropy addresses this by performing the same cross-entropy calculation of error, without requiring that the target variable be one hot encoded prior to training.

### Kullback Leibler Divergence Loss
KL Divergence is a measure of how one probability distribution differs from a baseline distribution.
A KL divergence loss of 0 suggests the distributions are identical. In practice, the behavior of KL Divergence is very similar to cross-entropy. It calculates how much information is lost (in terms of bits) if the predicted probability distribution is used to approximate the desired target probability distribution.
More commonly used when using models that learn to approximate a more complex function than simply multi-class classification, such as in the case of an autoencoder used for learning a dense feature representation under a model that must reconstruct the original input. In this case, KL divergence loss would be preferred.

# **[CS231n notes on linear classification](https://cs231n.github.io/linear-classify/)**

Sometimes also referred to as the **cost function** or the **objective**
Intuitively, the loss will be high if we’re doing a poor job of classifying the training data, and it will be low if we’re doing well.

> [!NOTE] The loss function quantifies our unhappiness with predictions on the training set

> [!NOTE] Two components of Loss Function
> Data Loss + Regularization Loss

## Loss Functions
### Multiclass Support Vector Machine -> Hinge Loss

> [!NOTE] Also referred to as Max-Margin Loss

The score function takes the pixels and computes the vector $f(x_i,W)$ of class scores, which we will abbreviate to $s$. For example, the score for the j-th class is the j-th element: $s_j=f(x_i,W)_j$. The Multiclass SVM loss for the i-th example is then formalized as follows:
$L_i = \sum_{(j \neq y_i)} \max (0, s_j - s_{y_i} + \Delta)$
In summary, the SVM loss function wants the score of the correct class $y_i$ to be larger than the incorrect class scores by at least by $\Delta$. If this is not the case, we will accumulate loss.
the threshold at zero $max(0,−)$ function is often called the **hinge loss**. You’ll sometimes hear about people instead using the squared hinge loss SVM (or L2-SVM), which uses the form $max(0,−)^2$ that penalizes violated margins more strongly (quadratically instead of linearly). The unsquared version is more standard, but in some datasets the squared hinge loss can work better. This can be determined during cross-validation.

#### Regularization

There is one bug with the loss function. The learned set of W is not necessarily unique. One easy way to see this is that if some parameters **W** correctly classify all examples (so loss is zero for each example), then any multiple of these parameters $\lambda W$ where $\lambda >1$ will also give zero loss because this transformation uniformly stretches all score magnitudes and hence also their absolute differences.
The most common regularization penalty is the squared **L2** norm that discourages large weights through an elementwise quadratic penalty over all parameters:
$R(W) = \sum_k \sum_l W^2_{k,l}$
![[linear classification-2023-05-01-1.png]]
L2 penalty prefers smaller and more diffuse weight vectors, the final classifier is encouraged to take into account all input dimensions to small amounts rather than a few input dimensions and very strongly. As we will see later in the class, this effect can improve the generalization performance of the classifiers on test images and lead to less *overfitting*.
Note that biases do not have the same effect since, unlike the weights, they do not control the strength of influence of an input dimension. Therefore, it is common to only regularize the weights W but not the biases b.

### Softmax Classifier -> Cross-entropy Loss

It turns out that the SVM is one of two commonly seen classifiers. The other popular choice is the **Softmax classifier**, which has a different loss function. If you’ve heard of the binary Logistic Regression classifier before, the Softmax classifier is its generalization to multiple classes. Unlike the SVM which treats the outputs $f(x_i,W)$ as (uncalibrated and possibly difficult to interpret) scores for each class, the Softmax classifier gives a slightly more intuitive output (normalized class probabilities) and also has a probabilistic interpretation. In the Softmax classifier, the function mapping $f(x_i,W)$stays unchanged, but we now interpret these scores as the unnormalized log probabilities for each class and replace the *hinge loss* with a **cross-entropy loss** that has the form:
![[linear classification-2023-05-01-2.png]]
**Softmax function:** $f_j(z) = \frac{e^{f_{y_i}}}{\sum_j e^{f_j}}$

It takes a vector of arbitrary real-valued scores (in z) and squashes it to a vector of values between zero and one that sum to one.

**Cross-entropy:** $H(p,q)=-\sum_x p(x) \log q(x)$
Minimizing cross entropy loss is equivalent to minimizing the KL divergence between the two distributions.

Softmax classifier interprets the scores inside the output vector f as the unnormalized log probabilities. Exponentiating these quantities therefore gives the (unnormalized) probabilities, and the division performs the normalization so that the probabilities sum to one. In the probabilistic interpretation, we are therefore minimizing the negative log likelihood of the correct class, which can be interpreted as performing *Maximum Likelihood Estimation* (MLE). A nice feature of this view is that we can now also interpret the regularization term R(W) in the full loss function as coming from a Gaussian prior over the weight matrix W, where instead of MLE we are performing the *Maximum a posteriori* (MAP) estimation.

> [!NOTE] Technically it doesn’t make sense to talk about the “softmax loss”, since softmax is just the squashing function, but it is a relatively commonly used shorthand.

Probabilities computed by the Softmax classifier are better thought of as confidences where, similar to the SVM, the ordering of the scores is interpretable, but the absolute numbers (or their differences) technically are not.

> [!NOTE] Summary
> The loss function contains two components: The data loss computes the compatibility between the scores **f** and the labels **y**. The regularization loss is only a function of the weights.

## Regularization
### L2

Perhaps the most common form of regularization
Can be implemented by penalizing the squared magnitude of all parameters directly in the objective.
For every weight w in the network, we add the term $\frac{1}{2}\lambda w^2$ to the objective, where λ is the regularization strength.
Intuitive interpretation of heavily penalizing peaky weight vectors and preferring diffuse weight vectors.
Appealing property of encouraging the network to use all of its inputs a little rather than some of its inputs a lot.
During gradient descent parameter update, using the L2 regularization ultimately means that every weight is decayed linearly: `W += -lambda * W` towards zero.

### L1

Has the intriguing property that it leads the weight vectors to become sparse during optimization (i.e. very close to exactly zero). In other words, neurons with L1 regularization end up using only a sparse subset of their most important inputs and become nearly invariant to the “noisy” inputs. In comparison, final weight vectors from L2 regularization are usually diffuse, small numbers. In practice, if you are not concerned with explicit feature selection, L2 regularization can be expected to give superior performance over L1.

### Max-norm Constraint

enforce an absolute upper bound on the magnitude of the weight vector for every neuron and use projected gradient descent to enforce the constraint.
One of its appealing properties is that network cannot “explode” even when the learning rates are set too high because the updates are always bounded.

### Dropout

While training, dropout is implemented by only keeping a neuron active with some probability p (a hyperparameter), or setting it to zero otherwise.

Can be interpreted as sampling a Neural Network within the full Neural Network, and only updating the parameters of the sampled network based on the input data. (However, the exponential number of possible sampled networks are not independent because they share the parameters.) During testing there is no dropout applied, with the interpretation of evaluating an averaged prediction across the exponentially-sized ensemble of all sub-networks
Because neurons are sampled and dropped randomly, the overall activation outout of the network will be reduced. Therefore the activations of the network need to be proportionally scaled when dropout is not applied at test time.
Since test-time performance is so critical, it is always preferable to use **inverted dropout**, which performs the scaling at train time, leaving the forward pass at test time untouched. Additionally, this has the appealing property that the prediction code can remain untouched when you decide to tweak where you apply dropout, or if at all.

### Bias Regularization

it is not common to regularize the bias parameters because they do not interact with the data through multiplicative interactions, and therefore do not have the interpretation of controlling the influence of a data dimension on the final objective. However, in practical applications (and with proper data preprocessing) regularizing the bias rarely leads to significantly worse performance

> [!TIP]
> It is most common to use a single, global L2 regularization strength that is cross-validated. It is also common to combine this with dropout applied after all layers. The value of p=0.5 is a reasonable default, but this can be tuned on validation data.

## Tasks
### Binary Classifier

$L_i = \max(0, 1 - y_{i}f(.))$

### Classification

Most common to use [[#Multiclass Support Vector Machine -> Hinge Loss]] or [[#Softmax Classifier -> Cross-entropy Loss]]
When the set of labels is very large (e.g. words in English dictionary, or ImageNet which contains 22,000 categories), computing the full softmax probabilities becomes expensive.
it may be helpful to use *Hierarchical Softmax* in natural language processing tasks (see one explanation [here](http://arxiv.org/pdf/1310.4546.pdf))

### Attribute Classification

Both losses above assume that there is a single correct answer $y_i$. But what if $y_i$ is a binary vector where every example may or may not have a certain attribute, and where the attributes are not exclusive?

#### Binary Classifier for Every Attribute

A sensible approach in this case is to build a binary classifier for every single attribute independently. For example, a binary classifier for each category independently would take the form:

$L_i = \sum_j\max(0, 1 - y_{ij}f_j)$
where the sum is over all categories $j$, and $y_{ij}$ is either +1 or -1 depending on whether the i-th example is labeled with the j-th attribute, and the score vector $f_j$ will be positive when the class is predicted to be present and negative otherwise. Notice that loss is accumulated if a positive example has score less than +1, or when a negative example has score greater than -1.

#### Logistic Regression for Every Attribute

An alternative to this loss would be to train a logistic regression classifier for every attribute independently. Minimize the negative log-likelihood
$L_i = -\sum_j y_{ij} \log(\sigma(f_j)) + (i - y_{ij})\log(1-\sigma(f_j))$
where the labels $y_{ij}$ are assumed to be either 1 (positive) or 0 (negative), and σ(⋅) is the sigmoid function. The expression above can look scary but the gradient on $f$ is in fact extremely simple and intuitive:
$\partial L_i / \partial f_j = \sigma(f_j) - y_{ij}$

### Regression

Task of predicting real-valued quantities, such as the price of houses or the length of something in an image.
common to compute the loss between the predicted quantity and the true answer and then measure the L2 squared norm, or L1 norm of the difference. The L2 norm squared would compute the loss for a single example of the form:
$L_i = ||f - y_i||_2^2$

L2 norm is preferred because it makes the gradient much simpler.
Looking at only the $j$-th dimension of the $i$-th example and denoting the difference between the true and the predicted value by $δ_{ij}$ the gradient for this dimension (i.e. $∂L_i/∂f_j$) is easily derived to be either $δ_{ij}$ with the L2 norm, or $sign(δ_{ij})$. That is, the gradient on the score will either be directly proportional to the difference in the error, or it will be fixed and only inherit the sign of the difference.

> [!WARNING] Prefer Classification over Regression
> L2 loss is much harder to optimize than a more stable loss such as Softmax. Intuitively, it requires a very fragile and specific property from the network to output exactly one correct value for each input (and its augmentations). Notice that this is not the case with Softmax, where the precise value of each score is less important: It only matters that their magnitudes are appropriate. Additionally, the L2 loss is less robust because outliers can introduce huge gradients. When faced with a regression problem, first consider if it is absolutely inadequate to quantize the output into bins.

### Structured Prediction

The structured loss refers to a case where the labels can be arbitrary structures such as graphs, trees, or other complex objects. Usually it is also assumed that the space of structures is very large and not easily enumerable.
