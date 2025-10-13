---
aliases: [cnn, conv nets, convolutional neural networks]
created: 2020-09-26-Saturday 09:40
modified: 2023-05-22-Monday 07:45
tags: aiml 
---

---

# CS231 Notes

[Good overall view](https://cs231n.github.io/convolutional-networks/) of [[neural networks]] and [[convolutional neural nets]]
![[convolutional neural nets-2023-05-02.png]]

- A ConvNet is made up of Layers. Every Layer has a simple API: It transforms an input 3D volume to an output 3D volume with some differentiable function that may or may not have parameters.
- We use three main types of layers to build ConvNet architectures: **Convolutional Layer**, **Pooling Layer**, and **Fully-Connected Layer** (exactly as seen in regular Neural Networks). We will stack these layers to form a full ConvNet **architecture**.
- CONV layer will compute the output of neurons that are connected to local regions in the input, each computing a dot product between their weights and a small region they are connected to in the input volume. This may result in volume such as [32x32x12] if we decided to use 12 filters.
- POOL layer will perform a downsampling operation along the spatial dimensions (width, height), resulting in volume such as [16x16x12].
- We will connect each neuron to only a local region of the input volume. The spatial extent of this connectivity is a hyperparameter called the **receptive field** of the neuron (equivalently this is the filter size). The extent of the connectivity along the depth axis is always equal to the depth of the input volume. It is important to emphasize again this asymmetry in how we treat the spatial dimensions (width and height) and the depth dimension: The connections are local in 2D space (along width and height), but always full along the entire depth of the input volume.

Convolution:
`(W-F+2P)/S + 1`
W is the input volume width/height,
F is filter size,
P is amount of zero padding and
S is the stride.

- Sizing the ConvNets appropriately so that all the dimensions “work out” can be a real headache, which the use of zero-padding and some design guidelines will significantly alleviate.

1x1 convolution works because all convolutions are applied over all the input channels (so it is really a 1x1xC weight matrix). This is used to apply fully connected operations to the network.
To collapse an image to a fully connected layer, just apply a convolution with F=W and K output filters, where K is the number of neurons in the fully connected layer (eg 4096).

If the image is larger than what the network was designed for, then it is common to take a few crops of the image with a stride equal to the total reduction, and then average over that result. Reduction means the ratio between the input to the final patch right before the "collapsing" (F=W) convolution is applied.

Common conv net architectures look like:
`INPUT -> [[CONV -> RELU]*N -> POOL?]*M -> [FC -> RELU]*K -> FC`

Stacking CONV layers with tiny filters as opposed to having one CONV layer with big filters allows us to express more powerful features of the input, and with fewer parameters.

> [!TIP] Don't be a hero
> Use whatever architecture currently works best on ImageNet. Download a pretrained model and then finetune to your data / use-case

`P=(F-1)/2` preserves the input size during convolutions (only the output channels differ).

Pooling Layer's function is to progressively reduce the spatial size of the representation to reduce the amount of parameters and computation in the network, and hence to also control overfitting.
Pooling Layer operates independently on every depth slice of the input and resizes it spatially, using the **MAX** operation.

> [!NOTE] Most Common
> Pooling layer with filters of size 2x2 applied with a stride of 2 downsamples every depth slice in the input by 2 along both width and height, discarding 75% of the activations
## Computational Constraints

Three major sources of memory to keep track of:

- raw number of **activations** at every layer of the ConvNet, and also their gradients (of equal size). Usually, most of the activations are on the earlier layers of a ConvNet (i.e. first Conv Layers).
	- These are kept around because they are needed for backpropagation, but a clever implementation that runs a ConvNet only at test time could in principle reduce this by a huge amount, by only storing the current activations at any layer and discarding the previous activations on layers below.
	- Could also increase filter size in the first layer to a larger value like [7x7] or [11x11] with large stride to significantly reduce parameters (applicable during backpropagation since we need to hold onto the activations)\
- numbers that hold the network **parameters**, their gradients during backpropagation, and commonly also a step cache if the optimization is using momentum, Adagrad, or RMSProp. Therefore, the memory to store the parameter vector alone must usually be multiplied by a factor of at least 3 or so.
- **miscellaneous** memory, such as the image data batches
If your network doesn’t fit, a common heuristic to “make it fit” is to decrease the batch size, since most of the memory is usually consumed by the activations.

## Transfer Learning

Three major scenarios:

- **Pretrained models** : Take it and go - should classify all the classes that you care about.
- **ConvNet as fixed feature extractor** : Take a ConvNet pretrained on ImageNet (or some huge dataset), remove the last fully-connected layer (this layer’s outputs are the 1000 class scores for a different task like ImageNet), then treat the rest of the ConvNet as a fixed feature extractor for the new dataset. These features are called **CNN Codes**. Once you extract the D-dimensional codes, train a linear classifier for the new dataset.
- **Fine-tuning the ConvNet** : not only replace and retrain the classifier on top of the ConvNet on the new dataset, but to also fine-tune the weights of the pretrained network by continuing the backpropagation. It is possible to fine-tune all the layers of the ConvNet, or it’s possible to keep some of the earlier layers fixed (due to overfitting concerns) and only fine-tune some higher-level portion of the network.
	- ***Note*** - earlier features of a ConvNet contain more generic features (e.g. edge detectors or color blob detectors) that should be useful to many tasks, but later layers of the ConvNet becomes progressively more specific to the details of the classes contained in the original dataset.

Common rules of thumb:

- *New dataset is small and similar to original dataset* - train a linear classifier on the CNN codes.
- *New dataset is large and similar to the original dataset* - we have more data, we can have more confidence that we won’t overfit if we were to try to fine-tune through the full network.
- *New dataset is small but very different from the original dataset* - Since the data is small, it is likely best to only train a linear classifier. Since the dataset is very different, it might not be best to train the classifier form the top of the network, which contains more dataset-specific features. Instead, it might work better to train the SVM classifier from activations somewhere earlier in the network.
- *New dataset is large and very different from the original dataset* - Even though dataset is large in practice it is very often still beneficial to initialize with weights from a pretrained model. In this case, we would have enough data and confidence to fine-tune through the entire network.
It’s common to use a smaller learning rate for ConvNet weights that are being fine-tuned, in comparison to the (randomly-initialized) weights for the new linear classifier, since the weights might already be quite good.

# Common Architectures

## Resnet & Resnext
	[[PyTorch]] [implementation & models](https://pytorch.org/hub/pytorch_vision_resnet/)
	

According to [[diffusion model#Fast AI course Part 2]] - ResNet blocks can be added to the diffusion network to squish down the number of channels.

### Residual Block

![[resnet-1.png]]
	The core idea of ResNet is introducing a so-called “identity shortcut connection” that skips one or more layers. ResNet was not the first to make use of shortcut connections, [[Highway Network]] introduced gated shortcut connections. These parameterized gates control how much information is allowed to flow across the shortcut. Similar idea can be found in the [[LSTM]] cell. ResNet can be thought of as a special case of Highway Network.
![[resnet-2.png]]

### Resnext

Very similar to the [[Inception]] module, they both follow the split-transform-merge paradigm, except in this variant, the outputs of different paths are merged by adding them together, while in Inception they are depth-concatenated. Another difference is that in an Inception module, each path is different (1x1, 3x3 and 5x5 convolution) from each other, while in this architecture, all paths share the same topology. Introduces a [[hyper parameter]] called cardinality — the number of independent paths, to provide a new way of adjusting the model capacity. Experiments show that accuracy can be gained more efficiently by increasing the cardinality than by going deeper or wider. The authors state that compared to Inception, this novel architecture is easier to adapt to new datasets/tasks, as it has a simple paradigm and only one hyper-parameter to be adjusted, while [[Inception]] has many [[hyper parameters]] (like the kernel size of the convolutional layer of each path) to tune.

	![[resnext.png]]
	

There have also been some experiments with ''Deep Network with Stochastic Depth'' that randomly drops off layers during training or both training and at test time. Turns out the results don't degrade much by doing that.

[Good article](https://towardsdatascience.com/an-overview-of-resnet-and-its-variants-5281e2f56035)

## Vgg

### Inception Blocks

### Siamese Networks

### Visual Transformer Vit

[[*shiny-fm-datasets#Vector-Quantized Image Modeling with Improved VQGAN]]

### Semantic Segmentation

#### Hands on Code Reference

[meet-shah](https://github.com/meetshah1995/pytorch-semseg)
[mit-csail](https://github.com/CSAILVision/semantic-segmentation-pytorch)
[some unet implementation](https://github.com/usuyama/pytorch-unet)

---

#### Summary

Based on this [article](https://medium.com/beyondminds/a-simple-guide-to-semantic-segmentation-effcf83e7e54). An alternate good [article](https://towardsdatascience.com/semantic-segmentation-with-deep-learning-a-guide-and-code-e52fc8958823).

#### Classical Method

Using Conditional Random Fields ([[CRF]]). It helps to resolve smoothing over neighboring labels. The cost of assigning a state (or label, u) to a single pixel (x) is known as its unary cost. To model relationships between pixels, we also consider the cost of assigning a pair of labels `(u,v)` to a pair of pixels `(x,y)` known as the pairwise cost. We can consider pairs of pixels that are its immediate neighbors (Grid [[CRF]]) or we can consider all pairs of pixels in the image (Dense [[CRF]])

![[crf-cat.png]]

![[grid-dense-crf.png]]

#### Deep Learning Model Architectures

##### Fully [[convolutional neural nets]] (FCN)

Simplest and basic method. Use deeper and deeper convolutions to encode. Then start decode by upsampling (transposed convolutions or bilinear interpolation)

![[fcn-fig.png]]

##### U-net

Upgrade to the simple FCN by adding skip connections for each layer in the encoder with its corresponding decoder.

- this model predicts images of the same size as the input
- the model makes the input image go through several blocks of ResNet layers which halves the image size by 2
- then through the same number of blocks that upsample it again.
- skip connections link features on the downsample path to corresponding layers in the upsample path.
![[Pasted image 20221221062718.png|650]]
![[unet-fig.png]]

###### Multiscale Methods

**Pyramid Scene Parsing Network ([[PSPNet]]):**
Performs the pooling operation (max or average) using four different kernel sizes and strides to the output feature map of a CNN such as the [[ResNet]]. It then upsamples the size of all the pooling outputs and the CNN output feature map using bilinear interpolation, and concatenates all of them along the channel axis. A final convolution is performed on this concatenated output to generate the prediction.

![[pspnet-fig.png]]

***'Atrous (Dilated) Convolutions*** present an efficient method to combine features from multiple scales without increasing the number of parameters by a large amount. By adjusting the dilation rate, the same filter has its weight values spread out farther in space. This enables it to learn more global context. The [[DeepLabv3]] paper uses Atrous Convolutions with different dilation rates to capture information from multiple scales, without significant loss in image size. They experiment with using Atrous convolutions in a cascaded manner and also in a parallel manner in the form of Atrous Spatial Pyramid Pooling (as shown below).

![[deeplavv3-atrconv.png]]

##### [[loss functions]]

***Pixel-wise [[softmax]] with [[cross entropy]]:*** Labels are represented as one hot vectors and are the same size as the image. Model output is `CxHxW` where C are the number of classes.

Is there is heavy class imbalance, i.e a lot more background pixels vs foreground ones consider using [[Focal Loss]] (introduced in the [[RetinaNet]] paper). [[Focal Loss]] does not penalize the model to such a large extent when the model is confident about a class. Say if 97% of the image is background & 3% foreground and our model is 80% sure about pixels that are background, but only 30% sure about pixels that are the target class. While using cross-entropy, loss due to background pixels is equal to (97% of 10000) * 0.3 which equals 2850 and loss due to target pixels is equal to (3% of 10000) * 1.2 which equals 360. Clearly, the loss due to the more confident class dominates, and there is very low incentive for the model to learn the target class. Comparatively, with focal loss, loss due to background pixels is equal to (97% of 10000) * 0 which is 0. This allows the model to learn the target class better.
