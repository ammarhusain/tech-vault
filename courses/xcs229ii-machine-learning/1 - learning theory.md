---
aliases: [bias-variance tradeoff]
created: 2022-09-23-Friday 09:16
modified: 2023-03-13-Monday 16:24
tags: [aiml]
---


---

# Bias-variance Tradeoff

[[courses/xcs229ii-machine-learning/attachments/Learning_Theory.pdf]]
[[courses/xcs229ii-machine-learning/attachments/Bias-Variance_Addendum.pdf]]
[[courses/xcs229ii-machine-learning/attachments/Bias-Variance_and_Error_Analysis.pdf]]

Models with high bias tend to underfit

Models with high variance tend to overfit

High variance, means the model fit keeps changing with slight perturbation. Versus high bias means the model doesnt give a fuck and stays more or less the same.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923091839.png]]
There are two main assumptions in ML:

- There exists a distribution D from which all (both training and test) data (aka x-data and y-labels pairs) is sampled.
- Data is sampled independently i.i.d

From a parameter view when there are just to parameters theta1 and theta 2
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923091857.png]]
As the number of samples goes to infinity, the variance of the model goes to 0

Unbiased estimator is when the theta hat → theta star (optimal) and # of samples → infinity : this makes the model consistent.

Bias is when theta hat is far away from theta star

How to address variance?

- get more data
- regularization

# Regularization

[[courses/xcs229ii-machine-learning/attachments/Regularization_and_Model_Selection.pdf]]

Linear regression is a maximum likelihood estimator on a certain generalized linear model using a gaussian distribution.

With the bayesian view you are just assuming that my model parameters theta is sampled from some gaussian distribution with mean 0 and some variance tau. Some the regularization term is simply penalizing the model from going too far out from that mean.

You do not regularize per parameter but regularize the norm of the parameter vector itself. This reduces the hyperparameter lambda down to just one vs N where N is the dimensionality of theta.

A common preprocessing step to use in learning algorithms is to normalize your data.

## Train-dev-test Splits

Split your dataset into 3 parts: train, dev, and test sets

- Train each model on S_train. Get some hypothesis (learned algorithm or parameter values etc.)
- Measure error on S_dev. Pick the hypothesis model with the lowest error on dev set.
- Report error on S_test ... That reports true model accuracy (this would be equivalent to the eval datasets).

The model has of course seen the training data and is optimized given the dev dataset therefore it can be considered that the model has knowledge of both. However the test dataset will be completely novel and most often hidden.

Historically rule of thumb: 70% train, 30% test (if you don't need to do model selection) or may be 60% train, 20% dev and 20% test (where dev helps with model selection).

Decent rules of thumb when you dont have massive datasets. But with huge datasets the number of examples going to dev and test sets is shrinking. Could be 90%, 5% & 5%

General advise: make the dev and test sets large enough where you can notice the performance differences (levels of accuracy etc) between different algorithms.

If you are working on production [[machine-learning]] systems, sometimes its ok not to have a test set to report the actual errors of the production system. You can just report the errors on the dev set. This is because your system will encounter all kinds of data in production anyway so no point going crazy trying to measure the true performance on some random held out test set. However this practice is not ok when reporting errors in academic papers that you are trying to publish.

## Model Selection and Cross Validation

Same PDF as Regularization section above.

The procedure described above with the train and dev set is called "hold out cross validation". The dev set is also sometime called the cross-validation set

If you have a small dataset use k-fold cross validation (typically k=10). Split the dataset in k splits and average the results.

Feature selection is a subset or special case of model selection. Just start with no features and incrementally start adding the most impactful feature one by one and retrain. Very simple algorithm.

k-fold cross validation is rarely used with deep learning because it just takes too long to train a neural net and they usually rely on a ton of data to work.

## Approximation and Estimation Errors

![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923092032.png|500]]
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923092041.png|500]]
By adding regularization you are effectively shrinking your class of hypotheses. So it can reduce variance but add more bias.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923092101.png|300]]

## Empirical risk Minimizer and Vc Dimension

Tools: (i) Union bound, (ii) Hoeffding's inequality
