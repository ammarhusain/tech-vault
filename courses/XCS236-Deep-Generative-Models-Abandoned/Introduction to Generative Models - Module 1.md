[[XCS236_Module_1_Slides.pdf]]
[Lecture Notes: Introduction](https://deepgenerativemodels.github.io/notes/introduction/)
[[XC236_Module_1_Lecture_Notes.pdf]]
[[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Learning Deep Generative Models Ruslan Salakhutdinov.pdf]]


![[Introduction to Generative Models - Module 1-2025-01-28.png]]
![[Introduction to Generative Models - Module 1-2025-01-28-1.png]]
![[Introduction to Generative Models - Module 1-2025-01-28-2.png]]
![[Introduction to Generative Models - Module 1-2025-01-28-3.png]]

Imitation Learning is a good usecase of Generative Models: P(actions | past observations)

![[Introduction to Generative Models - Module 1-2025-01-28-4.png]]

## Lecture 2
High level picture that comes up often in this course
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31.png]]
Need to start with a dataset -> define a model family -> similarity metric
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-2.png]]
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-1.png]]
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-3.png]]
Strong assumption : consider each pixel as an independent random variable (reduces the number of parameters to just N pixels in the image each pixel has one independent pixel value)
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-4.png]]
These rules give you an easy way to break down a complex probability distribution to something more manageable - underlies most autoregressive models
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-5.png]]

Big savings can be achieved using the Markovian assumption: just the previous token is sufficient to condition on, not the full history : `2n-1` params to represent the distribution

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-6.png]]
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-7.png]]
Simple idea : you condition a variable on a small subset of parent nodes rather than all other nodes in the graph. This gives you the ability to model the probability of a nde given some local interactions that affect that node the most. The conditionals are usually much simpler to represent.
Marginal probability is the absolute probability value of a certain variable - that is it is not dependent on anything else (either conditionally or jointly)


> [!tldr] Neural Networks FTW
> Will not use Bayesian Networks or Graphical models much in this class - mostly use neural networks for everything

### Generative vs Discriminative classifier
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-8.png]]

Naive Bayes: Not the best model but can work decently well in practice

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-9.png]]

In discriminative models - if you only care about P(Y | X) why bother trying to model the distribution over the features you are likely to see P(X) 

For discriminative models you assume that you can map the features to some function  that gives you their probability values (cannot just store them in a table anymore)
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-10.png]]
Discriminative models usually assume less about the underlying data which is why they perform better with more data. For example they do not assume that the features X are conditionally independent of each other which a generative Naive Bayer would do in contrast

Linear Dependence means that the decision boundary is a straight line

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-12.png]]

Generative models attempt to compute the full joint distribution between Y=label and X=data: P(Y, X) -> harder problem
Discriminative models on the other hand are only interested in P(Y | X)

Neural models provide a more expressive / weaker assumption that allows for non linear dependence
![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-13.png]]

![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/Introduction to Generative Models - Module 1-2025-01-31-14.png]]

All this mathematically complex machinery just works out of the box if X is a continuous variable rather than a discrete variable as well -> we move from storing learned data from tables and move to the world of X_i being a vector











