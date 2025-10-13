---
created: 2022-09-05-Monday 21:30
modified: 2023-03-10-Friday 23:15
---

[Metrics - Jupyter Notebook Viewer](https://nbviewer.org/github/cgpotts/cs224u/blob/master/evaluation_metrics.ipynb)
[Methods - Jupyter Notebook Viewer](https://nbviewer.org/github/cgpotts/cs224u/blob/master/evaluation_methods.ipynb)

- Different evaluation metrics encoder different values and have different biases & other weaknesses.
- Sometimes there are established norms for the metrics a community uses. Feel free to argue with it if you think its not representative for your work.
- scikit-learn model evaluation usage guide is great!
- confusion matrix: this is not the space the model directly predicts in (outputs probabilities that get thresholded to a discrete class labels).
- Accuracy: simplest. # correct/# total predictions. Negatively correlated with the negative log (logistic, cross entropy) loss so classifier is inherently optimizing accuracy. $-\frac{1}{N}\sum_{i=1}^{N}\sum_{k=1}^{K}  y_{i,k}\log(p_{i,k})$

	 Can be problematic cuz of that.

	 - Does not give per-class metrics for multi-class problems. Fails to control for size imbalances among different classes in the dataset. I guess I ran into something similar with the loss around background labels when training sem seg.
	 - KL divergence is an analogue of accuracy for soft labels.
- Precision: sum of the correct prediction divided by the sun of all guesses. Diagonal values divided by the column sums of confusion matrix.
- Recall: sum of correct predictions divided by the sum of all true instances. Diagonal values divided by the row sums. Encoded a permissive value in penalizing only missed true cases.
- F-scores: Harmonic mean between precision & recall:

	 $(\beta^2 + 1).\frac{precision.recall}{(\beta^2.precision) + recall}$

	 F-1 is simply beta = 1 where precision & recall are weighted equally.

	 Weakness: does not encode the size of the dataset (not sure if it matters much generally).

- Dice similarity for binary vectors is sometimes used to asses how well a model has learned to identify a set of items. It is equivalent to the per token F1 score.
- Macro-averaged F-score: Just the average of all per class F-scores. (can also do weighted avg).
- Micro-averaged F-scores (pretty much same as accuracy)
- SNLI (dataset created with image captions as premise)
- Adversarial Training: not too much interesting here other than the fact that these really break models.
- Average precision: calculated by summing the precision weighted by the change in recall from step to step of the precision-recall curve. Is a discrete approximation of the area under the precision-recall curve.

# Evaluation Methods
- Traditional dataset split is train / dev / test

## Cross Validation

In cross-validation, we take a set of examples $X$ and partition them into two or more train/test splits, and then we average over the results in some way.

**Random Splits**

When creating random train/test splits, we shuffle the examples and split them, with a pre-specified percentage $t$ used for training and another pre-specified percentage (usually $1−𝑡$) used for testing. However this does not guarantee that all training examples will be seen.

In general, we want these splits to be **stratified** in the sense that the train and test splits have approximately the same distribution over the classes.

**K-folds**

One divides the data into $k$ folds of equal size and then conducts $k$ experiments. In each, fold $i$ is used for assessment, and all the other folds are merged together for training

## Baselines Are Crucial for Strong Experiments

Evaluation numbers in NLP (and throughout AI) can never be understood properly in isolation. There could be some problems that just with random guessing achieve a super high score vs some that just have really low accuracy with a very smart system. Defining baselines should not be an afterthought, but rather central to how you define your overall hypotheses. **Baselines are essential to building a persuasive case**, and they can also be used to illuminate specific aspects of the problem and specific virtues of your proposed system.

**Random baselines**

Random baselines are almost always useful to include. scikit-learn has classes [DummyClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier) and [DummyRegressor](http://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor). Each of them has a keyword argument `strategy` that allows you to specify a range of different styles of random guessing. Highly recommend using these in your work.

Task-specific baselines

It is worth considering if the problem has some kind of structure that lends itself to some very simple baseline model that already does better than just randomly guessing. For example in the NLI task we used a hypothesis only baseline which turned out to perform much better than random guessing.

## Hyperparameter Optimization

**Parameters** of a model are those whose values are learned as part of optimizing the model itself.

**Hyperparameters** of a model are any settings that are set by a process that is outside of this optimization process. The boundary between a true setting of the model and a broader design choice will likely be blurry conceptually.

**The ideal hyperparameter optimization setting**

When evaluating a model, the ideal regime for hyperparameter optimization is as follows:

1. For each hyperparameter, identify a large set of values for it.
2. Create a list of all the combinations of all the hyperparameter values. This will be the [cross-product](https://en.wikipedia.org/wiki/Cartesian_product) of all the values for all the features identified at step 1.
3. For each of the settings, cross-validate it on the available training data.
4. Choose the settings that did best in step 3, train on all the training data using those settings, and then evaluate that model on the test set.

**Practical considerations, and some compromises**

Some pragmatic steps you can take to alleviate this problem, in descending order of attractiveness.

1. **Randomly sampling** from the space of hyperparameters delivers results like the full "grid search" described above with a relatively few number of samples. **Hyperparameter optimization algorithms** like those implemented in [Hyperopt](http://hyperopt.github.io/hyperopt/) and [scikit-optimize](https://github.com/scikit-optimize/scikit-optimize) allow guided sampling from the full space.
2. **Hyperparameter search could be done on the basis of just a few iterations**. The systems likely won't have converged, but it's a solid working assumption that early performance is highly predictive of final performance.
3. Not all hyperparameters will contribute equally to outcomes. Via heuristic exploration, it is typically possible to **identify the less informative ones and set them by hand**.
4. Where repeated train/test splits are being run, one might **find optimal hyperparameters via a single split** and use them for all the subsequent splits. This is justified if the splits are very similar.
5. In the worst case, one might have to adopt hyperparameters that were optimal for other experiments that have been published.

**Some handy scikit tools:** [model_selection](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection) package has classes `GridSearchCV` and `RandomizedSearchCV`. These are very easy to use. [scikit-optimize](https://github.com/scikit-optimize/scikit-optimize) offers a variety of methods for guided search through the grid of hyperparameters.

**Confidence intervals:** If you can afford to run the model multiple times, then reporting confidence intervals based on the resulting scores could suffice to build an argument about whether the models are meaningfully different. If you want a tabular representation, compute a **p-value**.

[**McNemar's test**](https://en.wikipedia.org/wiki/McNemar%27s_test) operates directly on the vectors of predictions for the two models being compared. It's like a confusion matrix for the 2 classifiers.

## Model Convergence

Neural networks models rarely converge, or they converge at different rates between runs, and their performance on the test data is often heavily dependent on these differences. Sometimes a model with a low final error turns out to be great, and sometimes it turns out to be worse than one that finished with a higher error. Who knows?!

**Incremental dev set testing**

The key to addressing this uncertainty is to **regularly collect information about dev set performance as part of training**. For example, after every epoch, one could make predictions on the dev set and store that vector of predictions, or just whatever assessment metric one is using. These assessments can provide direct information about how the model is doing on the actual task we care about, which will be a better indicator than the errors.

All the PyTorch models for this course accept a keyword argument `early_stopping`. The behavior should closely resemble that of `sklearn.neural_network` models. If `early_stopping=True`, then part of the dataset given to the `fit` method is reserved for incremental testing. The amount can be controlled with `validation_fraction` (default: `0.10`). After every epoch, this data will be used to evaluate the model using its `score` method. The parameters of the best model are stored. If an improvement of more than `tol` (default: `1e-5`) isn't seen within `n_iter_no_change` steps (default: `10`), then optimization stops, and the parameters of the numerically best model seen are used as the final model.

It's important to see just how different this dev set performance can be from the training loss. In particular, the training loss can continue to go down even as the model grows worse and worse in evaluations on held-out data. This is a common form of **over-fitting**.

- Dont take error/loss going down as a proxy for model performance/score increasing
