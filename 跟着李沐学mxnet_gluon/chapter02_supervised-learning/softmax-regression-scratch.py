
# coding: utf-8

# # Multiclass logistic regression from scratch
#
# If you've made it through our tutorial on linear regression from scratch, then you're past the hardest part. You already know how to load and manipulate data, build computation graphs on the fly, and take derivatives. You also know how to define a loss function, construct a model, and write your own optimizer.
#
# Nearly all neural networks that we'll build in the real world consist of these same fundamental parts. The main differences will be the type and scale of the data, and the complexity of the models. And every year or two, a new hipster optimizer comes around, but at their core they're all subtle variations of stochastic gradient descent.
#
# So let's work on a more interesting problem now. We're going to classify images of handwritten digits like these:
# ![png](https://raw.githubusercontent.com/dmlc/web-data/master/mxnet/example/mnist.png)
# We're going to implement a model called multiclass logistic regression. Other common names for this model include softmax regression and multinomial regression. To start, let's import our bag of libraries.

# In[1]:


from __future__ import print_function
import mxnet as mx
from mxnet import nd, autograd
import numpy as np


# We'll also want to set the compute context for our modeling. Feel free to go ahead and change this to mx.gpu(0) if you're running on an appropriately endowed machine.

# In[2]:


ctx = mx.cpu()


# ## The MNIST dataset
#
# This time we're going to work with real data, each a 28 by 28 centrally cropped black & white photograph of a handwritten digit. Our task will be come up with a model that can associate each image with the digit (0-9) that it depicts.
#
# To start, we'll use MXNet's utility for grabbing a copy of this dataset. The datasets accept a transform callback that can preprocess each item. Here we cast data and label to floats and normalize data to range [0, 1]:

# In[3]:


def transform(data, label):
    return data.astype(np.float32)/255, label.astype(np.float32)
mnist_train = mx.gluon.data.vision.MNIST(train=True, transform=transform)
mnist_test = mx.gluon.data.vision.MNIST(train=False, transform=transform)


# There are two parts of the dataset for training and testing. Each part has N items and each item is a tuple of an image and a label:

# In[ ]:


image, label = mnist_train[0]
print(image.shape, label)


# Note that each image has been formatted as a 3-tuple (height, width, channel). For color images, the channel would have 3 dimensions (red, green and blue).

# ## Record the data and label shapes
#
# Generally, we don't want our model code to care too much about the exact shape of our input data. This way we could switch in a different dataset without changing the code that follows. Let's define variables to hold the number of inputs and outputs.
#

# In[ ]:


num_inputs = 784
num_outputs = 10


# Machine learning libraries generally expect to find images in (batch, channel, height, width) format. However, most libraries for visualization prefer (height, width, channel). Let's transpose our image into the expected shape. In this case, matplotlib expects either (height, width) or (height, width, channel) with RGB channels, so let's broadcast our single channel to 3.

# In[ ]:


im = mx.nd.tile(image, (1,1,3))
print(im.shape)


# Now we can visualize our image and make sure that our data and labels line up.

# In[ ]:


import matplotlib.pyplot as plt
plt.imshow(im.asnumpy())
plt.show()


# Ok, that's a beautiful five.

# ## Load the data iterator
#
# Now let's load these images into a data iterator so we don't have to do the heavy lifting.

# In[ ]:


batch_size = 1024
train_data = mx.gluon.data.DataLoader(mnist_train, batch_size, shuffle=True)


# We're also going to want to load up an iterator with *test* data. After we train on the training dataset we're going to want to test our model on the test data. Otherwise, for all we know, our model could be doing something stupid (or treacherous?) like memorizing the training examples and regurgitating the labels on command.

# In[ ]:


test_data = mx.gluon.data.DataLoader(mnist_test, batch_size, shuffle=False)


# ## Allocate model parameters
#
# Now we're going to define our model. For this example, we're going to ignore the multimodal structure of our data and just flatten each image into a single 1D vector with 28x28 = 784 components.
#
# Because our task is multiclass classification, we want to assign a probability to each of the classes P(Y=c|X) given the input X. In order to do this we're going to need one vector of 784 weights for each class, connecting each feature to the corresponding output. Because there are 10 classes, we can collect these weights together in a 784 by 10 matrix.
#
# We'll also want to allocate one offset for each of the outputs. We call these offsets the *bias term* and collect them in the 10-dimensional array ``b``.

# In[ ]:


W = nd.random_normal(shape=(num_inputs, num_outputs))
b = nd.random_normal(shape=num_outputs)

params = [W, b]


# As before, we need to let MXNet know that we'll be expecting gradients corresponding to each of these parameters during training.

# In[ ]:


for param in params:
    param.attach_grad()


# ## Multiclass logistic regression
#
# In the linear regression tutorial, we performed regression, so we had just one output *yhat* and tried to push this value as close as possible to the true target *y*. Here, instead of regression, we are performing *classification*, where we want to assign each input *X* to one of *L* classes.
#
# The basic modeling idea is that we're going to linearly map our input *X* onto 10 different real valued outputs ``y_linear``. Then before, outputting these values, we'll want to normalize them so that they are non-negative and sum to 1. This normalization allows us to interpret the output yhat as a valid probability distribution.
#
#

# In[ ]:


def softmax(y_linear):
    exp = nd.exp(y_linear-nd.max(y_linear))
    norms = nd.sum(exp, axis=0, exclude=True).reshape((-1,1))
    return exp / norms


# In[ ]:


sample_y_linear = nd.random_normal(shape=(2,10))
sample_yhat = softmax(sample_y_linear)
print(sample_yhat)


# Let's confirm that indeed all of our rows sum to 1.

# In[ ]:


print(nd.sum(sample_yhat, axis=1))


# But for small rounding errors, the function works as expected.

# ## Define the model
#
# Now we're ready to define our model

# In[ ]:


def net(X):
    y_linear = nd.dot(X, W) + b
    yhat = softmax(y_linear)
    return yhat


# ## The  cross-entropy loss function
#
# Before we can start training, we're going to need to define a loss function that makes sense when our prediction is a  probability distribution.
#
# The relevant loss function here is called cross-entropy and it may be the most common loss function you'll find in all of deep learning. That's because at the moment, classification problems tend to be far more abundant than regression problems.
#
# The basic idea is that we're going to take a target Y that has been formatted as a one-hot vector, meaning one value corresponding to the correct label is set to 1 and the others are set to 0, e.g. ``[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]``.
#
#
# The basic idea of cross-entropy loss is that we only care about how much probability the prediction assigned to the correct label. In other words, for true label 2, we only care about the component of yhat corresponding to 2. Cross-entropy attempts to maximize the log-likelihood given to the correct labels.

# In[ ]:


def cross_entropy(yhat, y, idx):
    if idx > 3:
        print("minimum yhat every row: ", yhat.asnumpy().min(axis=1))
    print("minimum yhat: %E" % yhat.asnumpy().min(axis=1).min())
    return - nd.sum(y * nd.log(yhat), axis=0, exclude=True)


# ## Optimizer
#
# For this example we'll be using the same stochastic gradient descent (SGD) optimizer as last time.

# In[ ]:


def SGD(params, lr):
    for param in params:
        param[:] = param - lr * param.grad


# ## Write evaluation loop to calculate accuracy
#
# While cross-entropy is nice, differentiable loss function, it's not the way humans usually evaluate performance on multiple choice tasks. More commonly we look at accuracy, the number of correct answers divided by the total number of questions. Let's write an evaluation loop that will take a data iterator and a network, returning the model's accuracy  averaged over the entire dataset.

# In[ ]:


def evaluate_accuracy(data_iterator, net):
    numerator = 0.
    denominator = 0.
    for i, (data, label) in enumerate(data_iterator):
        data = data.as_in_context(ctx).reshape((-1,784))
        label = label.as_in_context(ctx)
        label_one_hot = nd.one_hot(label, 10)
        output = net(data)
        predictions = nd.argmax(output, axis=1)
        numerator += nd.sum(predictions == label)
        denominator += data.shape[0]
    return (numerator / denominator).asscalar()


# Because we initialized our model randomly, and because roughly one tenth of all examples belong to each of the ten classes, we should have an accuracy in the ball park of .10.

# In[ ]:


evaluate_accuracy(test_data, net)


# ## Execute training loop

# In[ ]:


epochs = 1
moving_loss = 0.
learning_rate = .00001
smoothing_constant = .01
niter=0

for e in range(epochs):
    for i, (data, label) in enumerate(train_data):
        data = data.as_in_context(ctx).reshape((-1,784))
        label = label.as_in_context(ctx)
        label_one_hot = nd.one_hot(label, 10)
        with autograd.record():
            print("batch: %d, lr: %.4f" % (i, learning_rate))
            output = net(data)
            print("output or yhat min:", output.asnumpy().min())
            loss = cross_entropy(output, label_one_hot, i)
            print("loss: %.4f" % (nd.mean(loss).asscalar()))
        loss.backward()
        if i % 2 == 0: # 每2batch,放大learning_rate*10
            learning_rate *= 10
        if i > 8:
            break

        SGD(params, learning_rate)

        ##########################
        #  Keep a moving average of the losses
        ##########################
        niter +=1
        moving_loss = (1 - smoothing_constant) * moving_loss + (smoothing_constant) * nd.mean(loss).asscalar()
        est_loss = moving_loss/(1-(1-smoothing_constant)**niter)


    test_accuracy = evaluate_accuracy(test_data, net)
    train_accuracy = evaluate_accuracy(train_data, net)
    print("Epoch %s. Loss: %s, Train_acc %s, Test_acc %s" % (e, est_loss, train_accuracy, test_accuracy))


# ## Using the model for prediction
# Let's make it more intuitive by picking 10 random data points from the test set and use the trained model for predictions.

# In[ ]:


# Define the function to do prediction
def model_predict(net,data):
    output = net(data)
    return nd.argmax(output, axis=1)

# let's sample 10 random data points from the test set
sample_data = mx.gluon.data.DataLoader(mnist_test, 10, shuffle=True)
for i, (data, label) in enumerate(sample_data):
    data = data.as_in_context(ctx)
    print(data.shape)
    im = nd.transpose(data,(1,0,2,3))
    im = nd.reshape(im,(28,10*28,1))
    imtiles = nd.tile(im, (1,1,3))

    plt.imshow(imtiles.asnumpy())
    plt.show()
    pred=model_predict(net,data.reshape((-1,784)))
    print('model predictions are:', pred)
    break


# ## Conclusion
#
# Jeepers. We can get nearly 90% accuracy at this task just by training a linear model for a few seconds! You might reasonably conclude that this problem is too easy to be taken seriously by experts.
#
# But until recently, many papers (Google Scholar says 13,800) were published using results obtained on this data. Even this year, I reviewed a paper whose primary achievement was an (imagined) improvement in performance. While MNIST can be a nice toy dataset for testing new ideas, we don't recommend writing papers with it.

# ## Next
# [Softmax regression with gluon](../chapter02_supervised-learning/softmax-regression-gluon.ipynb)

# For whinges or inquiries, [open an issue on  GitHub.](https://github.com/zackchase/mxnet-the-straight-dope)
