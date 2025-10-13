---
created: 2023-05-02-Tuesday 07:53
modified: 2023-05-02-Tuesday 07:54
publish: 
---

# [CS231n Notes](https://cs231n.github.io/neural-networks-2/#intro)
Three common forms of data preprocessing a data matrix `X`, where we will assume that `X` is of size `[N x D]` (`N` is the number of data, `D` is their dimensionality)

## Mean Subtraction
Involves subtracting the mean across every individual _feature_ in the data, and has the geometric interpretation of centering the cloud of data around the origin along every dimension.
`X -= np.mean(X, axis = 0)`
For images - it is also common to subtract a single pixel value from across the image or across every image channel.

## Normalization
Make the data dimensions of approximately the same scale. Two common ways:
- Divide each dimenstion by its standard deviations once it has been zero-centered: `X /= np.std(X, axis-0)`
- Normalize each dimension so that the min and max along the dimension is -1 and 1.
Only makes sense to normalize if different input features have different scales (or units).


![[data preprocessing-2023-05-02.png|400]]
## PCA
Compute the covariance matrix of the data matrix X that tells us about the correlation structure between the features in the data.
```python
# Assume input data matrix X of size [N x D]
X -= np.mean(X, axis = 0) # zero-center the data (important)
cov = np.dot(X.T, X) / X.shape[0] # get the data covariance matrix
```
The (i,j) element of the data covariance matrix contains the _covariance_ between i-th and j-th dimension of the data. Diagonal of this matrix contains the variances.

We could decorrelate the data by computing the SVD factorization:
`U,S,V = np.linalg.svd(cov)`
where the columns of `U` are the eigenvectors and `S` is a 1-D array of the singular values.
To decorrelate the data, we project the original (but zero-centered) data into the eigenbasis:
```python
Xrot = np.dot(X, U) # decorrelate the data
```
The projection therefore corresponds to a rotation of the data in `X` so that the new axes are the eigenvectors. If we were to compute the covariance matrix of `Xrot`, we would see that it is now diagonal.

We could also pick the top K largest eigenvalues to rotate the data matrix on corresponding to features that have the largest variance.
```python
Xrot_reduced = np.dot(X, U[:,:K]) # Xrot_reduced becomes [N x K]
```

It is very often the case that you can get very good performance by training linear classifiers or neural networks on the PCA-reduced datasets, obtaining savings in both space and time.

## Whitening

Takes the data in the eigenbasis and divides every dimension by the eigenvalue to normalize the scale. The geometric interpretation of this transformation is that if the input data is a multivariable gaussian, then the whitened data will be a gaussian with zero mean and identity covariance matrix. This step would take the form:

```python
# whiten the data:
# divide by the eigenvalues (which are square roots of the singular values)
Xwhite = Xrot / np.sqrt(S + 1e-5)
```


> [!WARNING] Exaggerating noise.
> One weakness of this transformation is that it can greatly exaggerate the noise in the data, since it stretches all dimensions (including the irrelevant dimensions of tiny variance that are mostly noise) to be of equal size in the input. This can in practice be mitigated by stronger smoothing (i.e. increasing 1e-5 to be a larger number).

![[data preprocessing-2023-05-02-1.png]]

![[data preprocessing-2023-05-02-2.png]]


> [!TIP] We mention PCA/Whitening in these notes for completeness, but these transformations are not used with Convolutional Networks. However, it is very important to zero-center the data, and it is common to see normalization of every pixel as well.

> [!TIP] An important point to make about the preprocessing is that any preprocessing statistics (e.g. the data mean) must only be computed on the training data, and then applied to the validation / test data.