![[courses/XCS236-Deep-Generative-Models-Abandoned/attachments/pytorch_tutorial.ipynb]]

Tensors are just a list of numbers or arrays -multi dimenesional arrays
One of the cool things with [[pytorch]] is AutoGrad
required_grad can be False during inference time because it is a lot of unneeded computation since we are not doing any gradient descent optimization
We can use `nn.Linear(H_in, H_out)` to create a a linear layer. This will take a matrix of `(N, *, H_in)` dimensions and output a matrix of `(N, *, H_out)`. The `*` denotes that there could be arbitrary number of dimensions in between. The linear layer performs the operation `Ax+b`, where `A` and `b` are initialized randomly.
First dimension is usually the batch dimension

Simplest neural network example in Pytorch:
```python
class MultilayerPerceptron(nn.Module):
	def __init__(self, input_size, hidden_size):
		# Call to the __init__ function of the super class
		super(MultilayerPerceptron, self).__init__()
		
		# Bookkeeping: Saving the initialization parameters
		self.input_size = input_size
		self.hidden_size = hidden_size
		
		# Defining of our model.There isn't anything specific about the naming of `self.model`. It could be something arbitrary.
		self.model = nn.Sequential(
			nn.Linear(self.input_size, self.hidden_size),
			nn.ReLU(),
			nn.Linear(self.hidden_size, self.input_size),
			nn.Sigmoid()
		)
	
	def forward(self, x):
		output = self.model(x)
		return output
```

```python
# Instantiate the model
model = MultilayerPerceptron(5, 3)
# Define the optimizer
adam = optim.Adam(model.parameters(), lr=1e-1)
# Define loss using a predefined loss function
loss_function = nn.BCELoss()
# Calculate how our model is doing now
y_pred = model(x)
loss_function(y_pred, y).item()
```

```python
# Set the number of epoch, which determines the number of training iterations
n_epoch = 10

for epoch in range(n_epoch):
	# Set the gradients to 0
	adam.zero_grad()
	
	# Get the model predictions
	y_pred = model(x)
	
	# Get the loss
	loss = loss_function(y_pred, y)
	
	# Print stats
	print(f"Epoch {epoch}: traing loss: {loss}")
	
	# Compute the gradients
	loss.backward()
	
	# Take a step to optimize the weights
	adam.step()
```