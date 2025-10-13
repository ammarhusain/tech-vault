---
aliases: [linear classifier]
created: 2023-05-01-Monday 10:13
modified: 2023-05-01-Monday 15:47
---

# **[CS231n notes on linear classification](https://cs231n.github.io/linear-classify/)**

Two major components:

- a **score function** that maps the raw data to class scores,
- and a **[[loss function]]** that quantifies the agreement between the predicted scores and the ground truth labels.
We will then cast this as an optimization problem in which we will minimize the loss function with respect to the parameters of the score function.

## Parameterized Mapping from Images to Label Scores

Define the score function that maps the pixel values of an image to confidence scores for each class.
Lets define a score function: $f:R^D\mapsto R^K$ where $D$ is the dimensionality of the input data and $K$ is the # of classes. For CIFAR-10 dataset N=50k images, each with D=32 x 32 x 3 = 3072 pixels and K=10 classes.

### Linear Classifier

This is arguable the simplest possible function, a linear mapping:
$f(x_i, W, b) = Wx_i + b$
we are assuming that the image $x_i$ has all of its pixels flattened out to a single column vector of shape [D x 1]. The matrix **W** (of size [K x D]), and the vector **b** (of size [K x 1]) are the **parameters** of the function. The parameters in **W** are often called the **weights**, and **b** is called the **bias vector** because it influences the output scores, but without interacting with the actual data $x_i$.

every row of $W$ is a classifier for one of the classes.

#### Geometric Interpretation

The geometric interpretation of these numbers is that as we change one of the rows of $W$, the corresponding line in the pixel space will rotate in different directions. The biases $b$, on the other hand, allow our classifiers to translate the lines. In particular, note that without the bias terms, plugging in $x_i=0$ would always give score of zero regardless of the weights, so all lines would be forced to cross the origin.

#### Template Matching Interpretation

Another interpretation for the weights $W$ is that each row of $W$ corresponds to a *template* (or sometimes also called a *prototype*) for one of the classes. The score of each class for an image is then obtained by comparing each template with the image using an *inner product* (or *dot product*) one by one to find the one that “fits” best. With this terminology, the linear classifier is doing template matching, where the templates are learned. Another way to think of it is that we are still effectively doing Nearest Neighbor, but instead of having thousands of training images we are only using a single image per class (although we will learn it, and it does not necessarily have to be one of the images in the training set), and we use the (negative) inner product as the distance instead of the L1 or L2 distance.
![[linear classification-2023-05-01.png]]

#### Image Data Preprocessing

it is important to **center your data** by subtracting the mean from every feature. In the case of images, this corresponds to computing a *mean image* across the training images and subtracting it from every image to get images where the pixels range from approximately [-127 … 127]. Further common preprocessing is to scale each input feature so that its values range from [-1, 1]. This is important to get the dynamics of gradient descent to work.

## Loss Function

[[loss function#**[CS231n notes on linear classification](https://cs231n.github.io/linear-classify/)**|CS231n notes on Hinge & Cross Entropy loss]]

## Summary
- Unlike kNN classifier, the advantage of this **parametric approach** is that once we learn the parameters we can discard the training data. Additionally, the prediction for a new test image is fast since it requires a single matrix multiplication with **W**, not an exhaustive comparison to every single training example.
