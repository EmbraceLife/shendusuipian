import numpy as np
import torch
from torch.autograd import Variable
###############################################################
from IPython.display import Latex
from IPython.display import Math
Latex("Let's mannually calcualte do/dx")
Math(r'z_i = 3(x_i+2)^2')
Math(r'o = \frac{1}{4}\sum_i z_i')
Math(r'\frac{do}{dz_i} = \frac{1}{4} \times (1+0)')


Math(r'\frac{dz_i}{dx_i} = (2 \times 3(x_i+2)^1)\times (1+0)')
Math(r'z_i\bigr\rvert_{x_i=1} = 27') # when x_i=1, z_i=27

Math(r'\frac{\partial o}{\partial x_i} = \frac{3\times2}{4}(x_i+2)')

Math(r'\frac{\partial o}{\partial x_i}\bigr\rvert_{x_i=1} = \frac{9}{2} = 4.5')

x = Variable(torch.ones(1, 2), requires_grad=True)
z = 3*(x+2)**2
o = torch.sum(z)/4
o.backward()
x.grad
###############################################################
# autograd make all the above mannual work gone !!!!
