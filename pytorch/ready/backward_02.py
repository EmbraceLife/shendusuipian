import numpy as np
import torch
from torch.autograd import Variable
###############################################################
from IPython.display import Latex
from IPython.display import Math

## backward() 注意事项 ###################################################
# x = torch.randn(3)
x = torch.ones(3).type(torch.FloatTensor)
x = Variable(x, requires_grad=True)

y = x * 2
while y.data.norm() < 1000:
    y = y * 2

print(y)

# y.backward()  #1. grad implicitly created only for scalar output


# 2. matching type and location|shape|size
gradients = torch.FloatTensor([0.1, 1.0, 0.01])
x

y.backward(gradients)

print(x.grad)
x.grad.data.zero_() # 3. This function accumulates gradients in the leaves - you might need to zero them before calling it.
y = y*2
