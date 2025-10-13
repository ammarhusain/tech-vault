---
aliases: []
tags:
---
# Precision-Recall Curves in Python

![rw-book-cover](https://machinelearningmastery.com/wp-content/uploads/2018/08/ROC-Curve-Plot-for-a-No-Skill-Classifier-and-a-Logistic-Regression-Model.png)
### Metadata
Author: [[Jason Brownlee]]
Full Title: Precision-Recall Curves in Python
Category: #readwise/articles
URL: https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/
Date Highlighted: [[2023-05-04-Thursday]]

## Highlights
- Two diagnostic tools that help in the interpretation of probabilistic forecast for binary (two-class) classification predictive modeling problems are **ROC Curves** and **Precision-Recall curves**.
  In this tutorial, you will discover ROC Curves, Precision-Recall Curves, and when to use each to interpret the prediction of probabilities for binary classification problems. ([View Highlight](https://read.readwise.io/read/01gzmg3qmpkwtazy2fjx7np051))
- ROC curves are appropriate when the observations are balanced between each class, whereas precision-recall curves are appropriate for imbalanced datasets. ([View Highlight](https://read.readwise.io/read/01gzmgb9j5st22vyw93674x7sw))
- A useful tool when predicting the probability of a binary outcome is the [Receiver Operating Characteristic curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic), or ROC curve.
  It is a plot of the false positive rate (x-axis) versus the true positive rate (y-axis) for a number of different candidate threshold values between 0.0 and 1.0. Put another way, it plots the false alarm rate versus the hit rate. ([View Highlight](https://read.readwise.io/read/01gzmgmp9b8sg8v0pe81jt6p9s))
- The true positive rate is calculated as the number of true positives divided by the sum of the number of true positives and the number of false negatives. It describes how good the model is at predicting the positive class when the actual outcome is positive. ([View Highlight](https://read.readwise.io/read/01gzmgtsdym2w689njj05dh980))
- The false positive rate is calculated as the number of false positives divided by the sum of the number of false positives and the number of true negatives. ([View Highlight](https://read.readwise.io/read/01gzmgvjdae282vxs87njmhram))
    - Note: TP | FP
      ---|---
      FN |TN
- • Smaller values on the x-axis of the plot indicate lower false positives and higher true negatives.
  • Larger values on the y-axis of the plot indicate higher true positives and lower false negatives. ([View Highlight](https://read.readwise.io/read/01gzmh0ssbqfx96mjrqthz2wf1))
    - Note: ROC curves:
      x-axis is false positive rate
      y-axis is true positive rate
- Precision is a ratio of the number of true positives divided by the sum of the true positives and false positives. It describes how good a model is at predicting the positive class. Precision is referred to as the positive predictive value. ([View Highlight](https://read.readwise.io/read/01gzmj71zexp6eca96tzb456qy))
- Recall is calculated as the ratio of the number of true positives divided by the sum of the true positives and the false negatives. Recall is the same as sensitivity. ([View Highlight](https://read.readwise.io/read/01gzmj7n2tz3vrmc3058t4ndbb))
- While the baseline is fixed with ROC, the baseline of [precision-recall curve] is determined by the ratio of positives (P) and negatives (N) as y = P / (P + N). ([View Highlight](https://read.readwise.io/read/01gzmjt15wg6wys850ke1eab3g))
- In terms of model selection, F-Measure summarizes model skill for a specific probability threshold (e.g. 0.5), whereas the area under curve summarize the skill of a model across thresholds, like ROC AUC. ([View Highlight](https://read.readwise.io/read/01gzmjwsw30n2fzh79nxym2271))
---
aliases: []
tags:
---
# Precision-Recall Curves in Python

![rw-book-cover](https://machinelearningmastery.com/wp-content/uploads/2018/08/ROC-Curve-Plot-for-a-No-Skill-Classifier-and-a-Logistic-Regression-Model.png)
### Metadata
Author: [[Jason Brownlee]]
Full Title: Precision-Recall Curves in Python
Category: #readwise/articles
URL: https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/
Date Highlighted: [[2023-05-04-Thursday]]

## Highlights
- Two diagnostic tools that help in the interpretation of probabilistic forecast for binary (two-class) classification predictive modeling problems are **ROC Curves** and **Precision-Recall curves**.
  In this tutorial, you will discover ROC Curves, Precision-Recall Curves, and when to use each to interpret the prediction of probabilities for binary classification problems. ([View Highlight](https://read.readwise.io/read/01gzmg3qmpkwtazy2fjx7np051))
- ROC curves are appropriate when the observations are balanced between each class, whereas precision-recall curves are appropriate for imbalanced datasets. ([View Highlight](https://read.readwise.io/read/01gzmgb9j5st22vyw93674x7sw))
- A useful tool when predicting the probability of a binary outcome is the [Receiver Operating Characteristic curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic), or ROC curve.
  It is a plot of the false positive rate (x-axis) versus the true positive rate (y-axis) for a number of different candidate threshold values between 0.0 and 1.0. Put another way, it plots the false alarm rate versus the hit rate. ([View Highlight](https://read.readwise.io/read/01gzmgmp9b8sg8v0pe81jt6p9s))
- The true positive rate is calculated as the number of true positives divided by the sum of the number of true positives and the number of false negatives. It describes how good the model is at predicting the positive class when the actual outcome is positive. ([View Highlight](https://read.readwise.io/read/01gzmgtsdym2w689njj05dh980))
- The false positive rate is calculated as the number of false positives divided by the sum of the number of false positives and the number of true negatives. ([View Highlight](https://read.readwise.io/read/01gzmgvjdae282vxs87njmhram))
    - Note: TP | FP
      ---|---
      FN |TN
- • Smaller values on the x-axis of the plot indicate lower false positives and higher true negatives.
  • Larger values on the y-axis of the plot indicate higher true positives and lower false negatives. ([View Highlight](https://read.readwise.io/read/01gzmh0ssbqfx96mjrqthz2wf1))
    - Note: ROC curves:
      x-axis is false positive rate
      y-axis is true positive rate
- Precision is a ratio of the number of true positives divided by the sum of the true positives and false positives. It describes how good a model is at predicting the positive class. Precision is referred to as the positive predictive value. ([View Highlight](https://read.readwise.io/read/01gzmj71zexp6eca96tzb456qy))
- Recall is calculated as the ratio of the number of true positives divided by the sum of the true positives and the false negatives. Recall is the same as sensitivity. ([View Highlight](https://read.readwise.io/read/01gzmj7n2tz3vrmc3058t4ndbb))
- While the baseline is fixed with ROC, the baseline of [precision-recall curve] is determined by the ratio of positives (P) and negatives (N) as y = P / (P + N). ([View Highlight](https://read.readwise.io/read/01gzmjt15wg6wys850ke1eab3g))
- In terms of model selection, F-Measure summarizes model skill for a specific probability threshold (e.g. 0.5), whereas the area under curve summarize the skill of a model across thresholds, like ROC AUC. ([View Highlight](https://read.readwise.io/read/01gzmjwsw30n2fzh79nxym2271))

