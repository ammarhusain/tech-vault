---
aliases: []
created: 2020-09-28-Monday 15:23
modified: 2023-03-10-Friday 23:15
tags: aiml 
---


---

Related: xcs224u [[courses/xcs224u - natural language understanding/5 - methods & metrics]]

# Rules of Thumb
For classification problems, usually the loss metric is cross entropy. But the value of cross entropy is not very intuitive. Therefore you may also want to keep track on the accuracy of prediction, true positive rate, precision, recall, F1 scores, and so on.

Mean Average Precision (mAP) is commonly used to analyze the performance of object detection and [segmentation](https://www.v7labs.com/blog/image-annotation-guide) systems.

# F-measure

[[neural networks]] [[convolutional neural nets]] [[metrics]]; [[scikit]]

F-measure is simply the harmonic mean between precision & recall.

[F-1 ](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)weights both precision & recall equally, while F-0.5 puts twice as much weight on precision.

By their nature F-measures are pessimistic so they tend to be closer to the lower of the 2 values.

$$
F1 = 2 . \frac{precision . recall}{precision + recall}
$$

# Precision-recall Curve
[[scikit]]
- Plots precision against recall
- [Precision-Recall curves](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html) should be used when there is a moderate to large class imbalance.
	- Specifically, there are many examples of no event (class 0) and only a few examples of an event (class 1). The reason for this is that typically the large number of class 0 examples means we are less interested in the skill of the model at predicting class 0 correctly, e.g. high true negatives.
- Recall is the same as "true-positive rate" from ROC curves
```python
# calculate precision-recall curve
precision, recall, thresholds = sklearn.metrics.precision_recall_curve(y, probs)

# F-Measure can be calculated by calling the f1_score() function that takes the true class values and the predicted class values as arguments.
# calculate F1 score
f1 = f1_score(testy, yhat) # yhat is obtained by thresholding probs at a certain probability value
```
![[metrics-2023-05-04-1.png]]
# Average Precision & Mean Average Precision
- Area under the precision-recall curve above.
- calculated as the weighted mean of precisions at each threshold; the weight is the increase in recall from the prior threshold.
- Mean Average Precision _is_ the average of AP of each class : $\frac{1}{N}\sum_{i=1}^N AP_i$
![[metrics-2023-05-06-2.png]]
![[metrics-2023-05-06-3.png]]
# Roc Curve
- Plots False-Positive Rate against True-Positive rate
- ROC curves should be used when there are roughly equal numbers of observations for each class. The reason for this recommendation is that ROC curves present an optimistic picture of the model on datasets with a class imbalance.
- scikit learn 
```python
# calculate roc curve
fpr, tpr, thresholds = sklearn.metrics.roc_curve(y, probs)
# The AUC for the ROC can be calculated using the [roc_auc_score()](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html) function.
```

![[metrics-2023-05-04.png|300]]

- ROC curves present an optimistic picture of the model on datasets with a class imbalance.
[good article](https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/)

# R^2 Score - Regression
 - Probably the most prominent method for summarizing regression model performance.

$$
\textbf{r2}(y, \widehat{y}) =
    1.0 - \frac{
      \sum_{i}^{N} (y_{i} - \hat{y_{i}})^{2}     
    }{
       \sum_{i}^{N} (y_{i} - \mu)^{2}
    }
$$    

where $\mu$ is the mean of the gold values $y$.

- Based in the ratio between what the model achieved and what its objective was, which is a measure of the goodness of fit of the model.
- Bounded between [0,1] which is nice compared with mean-squared error which is unbounded.

# Intersection over Union (IoU)
Indicates the overlap of the [predicted bounding box coordinates](https://www.v7labs.com/blog/bounding-box-annotation) to the ground truth box. Higher IoU indicates the predicted bounding box coordinates closely resembles the ground truth box coordinates.
![[metrics-2023-05-06.png]]

# Pearson Correlation
- [Pearson correlation coefficient $\rho$](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) between two vectors $y$ and $\widehat{y}$ of dimension $N$ is:

$$
\textbf{pearsonr}(y, \widehat{y}) = 
\frac{
  \sum_{i}^{N} (y_{i} - \mu_{y}) \cdot (\widehat{y}_{i} - \mu_{\widehat{y}})
}{
  \sum_{i}^{N} (y_{i} - \mu_{y})^{2} \cdot (\widehat{y}_{i} - \mu_{\widehat{y}})^{2}
}
$$

where $\mu_{y}$ is the mean of $y$ and $\mu_{\widehat{y}}$ is the mean of $\widehat{y}$.

- Bounded between [-1, 1] where -1 is a complete negative linear correlation, +1 is complete positive linear correlation and 0 is uncorrelated.
- Highly sensitive to the magnitude of difference between gold & predicted values. Consequently also sensitive to outliers (since the mean is used)

# Spearman Rank Correlation
- Is simply the [[Pearson correlation]] with data mapped to its ranks in the sequence. We used this metric in the HW#1 of the NLU class.
- Less sensitive to magnitude of the data and outliers since we map everything to relative ranks.
