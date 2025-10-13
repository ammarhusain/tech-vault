---
aliases: []
tags:
---
# Machine Learning Glossary

![rw-book-cover](https://www.gstatic.com/devrel-devsite/prod/v17bab36d69ae03fcc913f41eaedd7c01378ceed3d66f27cd213f7054697e46ba/developers/images/opengraph/white.png)
### Metadata
Author: [[Google Developers]]
Full Title: Machine Learning Glossary
Category: #readwise/articles
URL: https://developers.google.com/machine-learning/glossary
Date Highlighted: [[2023-10-12-Thursday]]

## Highlights
## accuracy
The number of correct classification [**predictions**](https://developers.google.com/machine-learning/glossary#prediction) divided by the total number of predictions.

Although a valuable metric for some situations, accuracy is highly misleading for others. Notably, accuracy is usually a poor metric for evaluating classification models that process [**class-imbalanced datasets**](https://developers.google.com/machine-learning/glossary#class_imbalanced_data_set).

[**Precision**](https://developers.google.com/machine-learning/glossary#precision) and [**recall**](https://developers.google.com/machine-learning/glossary#recall) are usually more useful metrics than **accuracy** for evaluating models trained on class-imbalanced datasets.

## activation function
  A function that enables [**neural networks**](https://developers.google.com/machine-learning/glossary#neural_network) to learn [**nonlinear**](https://developers.google.com/machine-learning/glossary#nonlinear) (complex) relationships between features and the label.
Popular activation functions include:

In a neural network, activation functions manipulate the [weighted sum](https://developers.google.com/machine-learning/glossary#weighted_sum) of all the inputs to a [neuron](https://developers.google.com/machine-learning/glossary#neuron).

## active learning
A [**training**](https://developers.google.com/machine-learning/glossary#training) approach in which the algorithm *chooses* some of the data it learns from. Active learning is particularly valuable when [**labeled examples**](https://developers.google.com/machine-learning/glossary#labeled_example) are scarce or expensive to obtain.

## AdaGrad
A sophisticated gradient descent algorithm that rescales the gradients of each [**parameter**](https://developers.google.com/machine-learning/glossary#parameter), effectively giving each parameter an independent [**learning rate**](https://developers.google.com/machine-learning/glossary#learning_rate).

## agent
In [**reinforcement learning**](https://developers.google.com/machine-learning/glossary#reinforcement_learning), the entity that uses a [**policy**](https://developers.google.com/machine-learning/glossary#policy) to maximize the expected [**return**](https://developers.google.com/machine-learning/glossary#return) gained from transitioning between [**states**](https://developers.google.com/machine-learning/glossary#state) of the [**environment**](https://developers.google.com/machine-learning/glossary#environment).

## anomaly detection
The process of identifying [**outliers**](https://developers.google.com/machine-learning/glossary#outliers). For example, if the mean for a certain [**feature**](https://developers.google.com/machine-learning/glossary#feature) is 100 with a standard deviation of 10, then anomaly detection should flag a value of 200 as suspicious.

## attention
Any of a wide range of [**neural network**](https://developers.google.com/machine-learning/glossary#neural_network) architecture mechanisms that aggregate information from a set of inputs in a data-dependent manner. A typical attention mechanism might consist of a weighted sum over a set of inputs, where the [**weight**](https://developers.google.com/machine-learning/glossary#weight) for each input is computed by another part of the neural network.

## AUC (Area under the ROC curve)
A number between 0.0 and 1.0 representing a [**binary classification**](https://developers.google.com/machine-learning/glossary#binary-classification) model's ability to separate [**positive classes**](https://developers.google.com/machine-learning/glossary#positive_class) from [**negative classes**](https://developers.google.com/machine-learning/glossary#negative_class). The closer the AUC is to 1.0, the better the model's ability to separate classes from each other.

AUC ignores any value you set for [**classification threshold**](https://developers.google.com/machine-learning/glossary#classification_threshold). Instead, AUC considers *all* possible classification thresholds.

## average precision
A metric for summarizing the performance of a ranked sequence of results.

## Bayesian neural network
A probabilistic [**neural network**](https://developers.google.com/machine-learning/glossary#neural_network) that accounts for uncertainty in [**weights**](https://developers.google.com/machine-learning/glossary#weight) and outputs. A standard neural network regression model typically [**predicts**](https://developers.google.com/machine-learning/glossary#prediction) a scalar value; for example, a standard model predicts a house price of 853,000. In contrast, a Bayesian neural network predicts a distribution of values; for example, a Bayesian model predicts a house price of 853,000 with a standard deviation of 67,200.

## classification threshold
In a [**binary classification**](https://developers.google.com/machine-learning/glossary#binary-classification), a number between 0 and 1 that converts the raw output of a [**logistic regression**](https://developers.google.com/machine-learning/glossary#logistic_regression) model into a prediction of either the [**positive class**](https://developers.google.com/machine-learning/glossary#positive_class) or the [**negative class**](https://developers.google.com/machine-learning/glossary#negative_class). Note that the classification threshold is a value that a human chooses, not a value chosen by model training.

The choice of classification threshold strongly influences the number of [**false positives**](https://developers.google.com/machine-learning/glossary#FP) and [**false negatives**](https://developers.google.com/machine-learning/glossary#FN).

## co-adaptation
When [**neurons**](https://developers.google.com/machine-learning/glossary#neuron) predict patterns in training data by relying almost exclusively on outputs of specific other neurons instead of relying on the network's behavior as a whole. When the patterns that cause co-adaption are not present in validation data, then co-adaptation causes overfitting. [**Dropout regularization**](https://developers.google.com/machine-learning/glossary#dropout_regularization) reduces co-adaptation because dropout ensures neurons cannot rely solely on specific other neurons.

## decoder
  In general, any ML system that converts from a processed, dense, or internal representation to a more raw, sparse, or external representation.
  Decoders are often a component of a larger model, where they are frequently paired with an [**encoder**](https://developers.google.com/machine-learning/glossary#encoder).
In [**sequence-to-sequence tasks**](https://developers.google.com/machine-learning/glossary#sequence-to-sequence-task), a decoder starts with the internal state generated by the encoder to predict the next sequence.

## embedding layer
A special [**hidden layer**](https://developers.google.com/machine-learning/glossary#hidden_layer) that trains on a high-dimensional [**categorical**](https://developers.google.com/machine-learning/glossary#categorical_data) feature to gradually learn a lower dimension embedding vector. An embedding layer enables a neural network to train far more efficiently than training just on the high-dimensional categorical feature.

## entropy
In [information theory](https://wikipedia.org/wiki/Information_theory), a description of how unpredictable a probability distribution is. Alternatively, entropy is also defined as how much information each [**example**](https://developers.google.com/machine-learning/glossary#example) contains. A distribution has the highest possible entropy when all values of a random variable are equally likely.

## federated learning
A distributed machine learning approach that [**trains**](https://developers.google.com/machine-learning/glossary#training) machine learning [**models**](https://developers.google.com/machine-learning/glossary#model) using decentralized [**examples**](https://developers.google.com/machine-learning/glossary#example) residing on devices such as smartphones. In federated learning, a subset of devices downloads the current model from a central coordinating server. The devices use the examples stored on the devices to make improvements to the model. The devices then upload the model improvements (but not the training examples) to the coordinating server, where they are aggregated with other updates to yield an improved global model. After the aggregation, the model updates computed by devices are no longer needed, and can be discarded.

In machine-learning image-detection tasks, IoU is used to measure the accuracy of the model's predicted [**bounding box**](https://developers.google.com/machine-learning/glossary#bounding_box) with respect to the [**ground-truth**](https://developers.google.com/machine-learning/glossary#ground_truth) bounding box. In this case, the IoU for the two boxes is the ratio between the overlapping area and the total area, and its value ranges from 0 (no overlap of predicted bounding box and ground-truth bounding box) to 1 (predicted bounding box and ground-truth bounding box have the exact same coordinates).

## logistic regression
  A type of [**regression model**](https://developers.google.com/machine-learning/glossary#regression_model) that predicts a probability. Logistic regression models have the following characteristics:
  • The label is [**categorical**](https://developers.google.com/machine-learning/glossary#categorical_data). The term logistic regression usually refers to **binary logistic regression**, that is, to a model that calculates probabilities for labels with two possible values. A less common variant, **multinomial logistic regression**, calculates probabilities for labels with more than two possible values.
  • The loss function during training is [**Log Loss**](https://developers.google.com/machine-learning/glossary#Log_Loss). (Multiple Log Loss units can be placed in parallel for labels with more than two possible values.)
• The model has a linear architecture, not a deep neural network. However, the remainder of this definition also applies to [**deep models**](https://developers.google.com/machine-learning/glossary#deep_model) that predict probabilities for categorical labels.

## logits
The vector of raw (non-normalized) predictions that a classification model generates, which is ordinarily then passed to a normalization function. If the model is solving a [**multi-class classification**](https://developers.google.com/machine-learning/glossary#multi-class) problem, logits typically become an input to the [**softmax**](https://developers.google.com/machine-learning/glossary#softmax) function. The softmax function then generates a vector of (normalized) probabilities with one value for each possible class.

## Markov decision process (MDP)
A graph representing the decision-making model where decisions (or [**actions**](https://developers.google.com/machine-learning/glossary#action)) are taken to navigate a sequence of [**states**](https://developers.google.com/machine-learning/glossary#state) under the assumption that the [**Markov property**](https://developers.google.com/machine-learning/glossary#Markov_property) holds. In [**reinforcement learning**](https://developers.google.com/machine-learning/glossary#reinforcement_learning), these transitions between states return a numerical [**reward**](https://developers.google.com/machine-learning/glossary#reward).

## minimax loss
A loss function for [**generative adversarial networks**](https://developers.google.com/machine-learning/glossary#generative_adversarial_network), based on the [**cross-entropy**](https://developers.google.com/machine-learning/glossary#cross-entropy) between the distribution of generated data and real data.

## PR AUC (area under the PR curve)
Area under the interpolated [**precision-recall curve**](https://developers.google.com/machine-learning/glossary#precision-recall_curve), obtained by plotting (recall, precision) points for different values of the [**classification threshold**](https://developers.google.com/machine-learning/glossary#classification_threshold). Depending on how it's calculated, PR AUC may be equivalent to the [**average precision**](https://developers.google.com/machine-learning/glossary#average_precision) of the model.

## precision-recall curve
A curve of [**precision**](https://developers.google.com/machine-learning/glossary#precision) vs. [**recall**](https://developers.google.com/machine-learning/glossary#recall) at different [**classification thresholds**](https://developers.google.com/machine-learning/glossary#classification_threshold).

## positional encoding
  A technique to add information about the *position* of a token in a sequence to the token's embedding. [**Transformer models**](https://developers.google.com/machine-learning/glossary#transformer) use positional encoding to better understand the relationship between different parts of the sequence.
A common implementation of positional encoding uses a sinusoidal function

## PR AUC (area under the PR curve)
Area under the interpolated [**precision-recall curve**](https://developers.google.com/machine-learning/glossary#precision-recall_curve), obtained by plotting (recall, precision) points for different values of the [**classification threshold**](https://developers.google.com/machine-learning/glossary#classification_threshold). Depending on how it's calculated, PR AUC may be equivalent to the [**average precision**](https://developers.google.com/machine-learning/glossary#average_precision) of the model.

## ROC (receiver operating characteristic) Curve
  A graph of [**true positive rate**](https://developers.google.com/machine-learning/glossary#TP_rate) vs. [**false positive rate**](https://developers.google.com/machine-learning/glossary#FP_rate) for different [**classification thresholds**](https://developers.google.com/machine-learning/glossary#classification_threshold) in binary classification.
The shape of an ROC curve suggests a binary classification model's ability to separate positive classes from negative classes.

![An ROC curve. The x-axis is False Positive Rate and the y-axis
  is True Positive Rate. The ROC curve approximates a shaky arc
  traversing the compass points from West to North.](https://developers.google.com/static/machine-learning/glossary/images/ROCTypicalGraph.png)
The point on an ROC curve closest to (0.0,1.0) theoretically identifies the ideal classification threshold. However, several other real-world issues influence the selection of the ideal classification threshold. For example, perhaps false negatives cause far more pain than false positives.

## quantile bucketing
Distributing a feature's values into [**buckets**](https://developers.google.com/machine-learning/glossary#bucketing) so that each bucket contains the same (or almost the same) number of examples.

## R-squared
A [**regression**](https://developers.google.com/machine-learning/glossary#regression_model) metric indicating how much variation in a [**label**](https://developers.google.com/machine-learning/glossary#label) is due to an individual feature or to a feature set. R-squared is a value between 0 and 1,

## Transformer
A [**neural network**](https://developers.google.com/machine-learning/glossary#neural_network) architecture developed at Google that relies on [**self-attention**](https://developers.google.com/machine-learning/glossary#self-attention) mechanisms to transform a sequence of input embeddings into a sequence of output embeddings without relying on [**convolutions**](https://developers.google.com/machine-learning/glossary#convolution) or [**recurrent neural networks**](https://developers.google.com/machine-learning/glossary#recurrent_neural_network). A Transformer can be viewed as a stack of self-attention layers.

## zero-shot learning
A type of machine learning [**training**](https://developers.google.com/machine-learning/glossary#training) where the [**model**](https://developers.google.com/machine-learning/glossary#model) infers a [**prediction**](https://developers.google.com/machine-learning/glossary#prediction) for a task that it was not specifically already trained on. In other words, the model is given zero task-specific training [**examples**](https://developers.google.com/machine-learning/glossary#example) but asked to do [**inference**](https://developers.google.com/machine-learning/glossary#inference) for that task.

