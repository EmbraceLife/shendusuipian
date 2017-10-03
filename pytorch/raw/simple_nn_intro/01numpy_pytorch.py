"""
http://pytorch.org/tutorials/beginner/examples_tensor/two_layer_net_numpy.html#sphx-glr-beginner-examples-tensor-two-layer-net-numpy-py

Warm-up: numpy
A fully-connected ReLU network with one hidden layer and no biases, trained to predict y from x using Euclidean error.

This implementation uses numpy to manually compute the forward pass, loss, and backward pass.

A numpy array is a generic n-dimensional array; it does not know anything about deep learning or gradients or computational graphs, and is just a way to perform generic numeric computations.
"""

import numpy as np
from IPython.display import Math
# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 64, 1000, 100, 10

# Create random input and output data
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

# Randomly initialize weights
w1 = np.random.randn(D_in, H) # 只要前后神经元个数不错就行，.T 解决位置问题
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(500):
    # Forward pass: compute predicted y
    h = x.dot(w1) # linear func
    h_relu = np.maximum(h, 0) # relu
    y_pred = h_relu.dot(w2) # linear (no activation)

    # Compute and print loss
    loss = np.square(y_pred - y).sum() # mse
    print(t, loss)

    # Backprop to compute gradients of w1 and w2 with respect to loss
    Math(r'\frac{dloss}{dy_{pred}} = \frac{dloss}{d(y_{pred}-y)} \times \frac{d(y_{pred}-y)}{dy_{pred}}= 2*(y_pred-y)^{2-1} \times (1-0)')
    grad_y_pred = 2.0 * (y_pred - y)

    Math(r'\frac{dloss}{dw^{[2]}} = \frac{dloss}{dy_{pred}} \times \frac{dy_{pred}}{dw^{[2]}}= 2*(y_pred-y) \times f\prime(hRelu_{0,0}\times w_{0,0}^{[2]} + hRelu_{0,1}\times w_{1,0}^{[2]} + \cdots)')


	# grad_y_pred (64,10), h_relu (64, 100)
    grad_w2 = h_relu.T.dot(grad_y_pred)
	# matrix ops, 内部一个值的grad公式，用于所有matrix中的值

    grad_h_relu = grad_y_pred.dot(w2.T) # w2 与 h_relu 功能相似，所以公式相似

    Math(r'\frac{dhRelu}{dh} = f\prime(max(h,0)) = \begin{cases} h,  & \text{if $h>0$} \\ 0, & \text{if $n<0$} \end{cases}')
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)

    # Update weights
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
