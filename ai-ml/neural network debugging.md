---
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
---

**Related:**
[[neural networks]]
[[courses/xcs229ii-machine-learning/2 - debugging ml algorithms]]

### Learnings
[[2024-06-20-Thursday]]
- Start with overfitting the heck out of a simple model to see if that even does what you want it to do.
	- #j595/meditation So important to be methodical and thinking step by step when training ML models rather than rush to expect a magical solution.
# [CS231n notes](https://cs231n.github.io/neural-networks-3/)
> [!TIP] **Overfit a tiny subset of data**
> Before training on the full dataset try to train on a tiny portion (e.g. 20 examples) of your data and make sure you can achieve zero cost. For this experiment it’s also best to set regularization to zero, otherwise this can prevent you from getting zero cost. Unless you pass this sanity check with a small dataset it is not worth proceeding to the full dataset.

## Gradient Checking
Comparing the numerical and analytical gradient with each other to make sure learning is happening correctly -> See [[optimization#Gradients]]
[Good article](https://cs231n.github.io/neural-networks-3/#gradcheck) with tips & tricks

## Loss Sanity Checking
- Make sure you’re getting the loss you expect when you initialize with small parameters. It’s best to first check the data loss alone (so set regularization strength to zero). For example, for CIFAR-10 with a Softmax classifier we would expect the initial loss to be 2.302, because we expect a diffuse probability of 0.1 for each class (since there are 10 classes), and Softmax loss is the negative log probability of the correct class so: -ln(0.1) = 2.302.

-   As a second sanity check, increasing the regularization strength should increase the loss

## Learning Process - Babysitting 

> [!TIP] Track over Epochs
> One epoch means that every example has been seen once. It is preferable to track epochs rather than iterations since the number of iterations depends on the arbitrary setting of batch size.
### Loss function
![[neural network debugging-2023-05-02.png|600]]
The amount of “wiggle” in the loss is related to the batch size. When the batch size is 1, the wiggle will be relatively high. When the batch size is the full dataset, the wiggle will be minimal because every gradient update should be improving the loss function monotonically (unless the learning rate is set too high).

Some people prefer to plot their loss functions in the log domain. Since learning progress generally takes an exponential form shape, the plot appears as a slightly more interpretable straight line, rather than a hockey stick.

### Training & Validation accuracy
![[neural network debugging-2023-05-02-1.png|650]]
### Other Fancier things to track
#### Ratio of weights / updates
A rough heuristic is that this ratio should be somewhere around 1e-3. If it is lower than this then the learning rate might be too low. If it is higher then the learning rate is likely too high.

#### Activation / Gradient distributions per layer
Intuitively, it is not a good sign to see any strange distributions - e.g. with tanh neurons we would like to see a distribution of neuron activations between the full range of [-1,1].

#### Layer Visualization
when one is working with image pixels it can be helpful and satisfying to plot the layer features visually
![[neural network debugging-2023-05-02-2.png|600]]

## Hyperparameter search
Good section [here](https://cs231n.github.io/neural-networks-3/#hyper)

> [!TIP] Title
> - Prefer random search to grid search
> - Search for hyperparameters on log scale
> - Single validation set of respectable size substantially simplifies the code base, without the need for cross-validation with multiple folds


# [StackExchange - What should I do when my neural network doesn't learn?](https://stats.stackexchange.com/questions/352036/what-should-i-do-when-my-neural-network-doesnt-learn)

- Step by step code & debug implementation, walking through and analyzing every piece from data loader & model to training pipeline. For eg: It was a good exercise to step through the conv2d and transposeConv2d operators to see how they are applied and how dimensions change when implementing de-noising autoencoder.
- Try and massively overfit the network to a small toy problem dataset. If it does not even overfit then something is off.
  - Reduce the number of images and the number of predicted labels.
- Step through by cooking up some data to make sure the loss values make sense/are reasonable.
- Look at not only the predicted & training labels but also the frequency of them to see if the network is at least finding the mode of that distribution.
- If the epoch loss is going down then the output label distribution is slowly shifting even though the predicted values (which is obtained by max()) stays the same. May be try and get the sense of the distribution by looking at the top 5 predictions.
- If there is class imbalance (too many of one kind of labels), then the loss function must be weighted accordingly, so that the network doesn't just learn the mode.
  - Alternatively look at variants of cross entropy loss eg; Focal Loss.
- Did you zero out the gradients?? Call .zero_grad() at the right place. If not they will explode!!

# [[GAN]]

[Good tips](https://github.com/soumith/ganhacks)

- Initially my discriminator loss would immediately collapse down to 0. I was able to alleviate this problem by setting soft target (0.7-1.2 for real & 0-0.3 for fake). It is also possible that my loss computation was all wrong since I pre initialized the ones & zeros vector, so there might have been some indexing bug.
  - Did another experiment with 0 & 1 this time initialized in loop and the loss collases to 0 for discriminator. I think with soft targets, given the randomness the loss is non zero but it is also actually collapsing, as in the the discriminator gets it right within a gradient step or 2. So the convergence keeps bouncing arouns and the loss is pretty steady for both generator & discriminator without much learning on the generator end.
	- Also dropped the sigmoid layer in the discriminator in favor of BCELossWithLogits instead of [[BCELoss]] as before. Apparently its more numerically stable.
  - Download the notebook from the blog post and that works great in a couple of epochs. Will dig deeper in there.
  - Fucking hell, turns out I just forgot to zero out gradients on the generator's optimizer which caused it to explode and training collapsed soon because the discriminator went straight down to 0.

[Instance Noise: A trick for stabilising GAN training](https://www.inference.vc/instance-noise-a-trick-for-stabilising-gan-training/)

[How to Identify and Diagnose GAN Failure Modes](https://machinelearningmastery.com/practical-guide-to-gan-failure-modes/)

# Gpu Memory Fragementation

 Unable to run a big batch size (~8) for a P5000 GPU with 12GB RAM. This is because of memory fragmentation.

Handy way to inspect is by `import pdb` and the do `pdb.set_trace()` through your code. In terminal run `watch -n 0.1 nvidia-smi` to inspect memory usage.

Inspect [[pytorch]] tensor size:
`tnsr_name.element_size()` and `tnsr_name.nelements()`
Total usage is `tnsr_name.element_size() * tnsr_name.nelements()`
