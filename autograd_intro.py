import plotly 


# introduction to autograd

# numpy function enabled by autograd
import autograd.numpy as np

# The only autograd function you may ever need
from autograd import grad

# create tanh
def tanh(x):
    y = np.exp(-x)
    return (1.0 - y) / (1.0 + y)

def eg_intro():
	# Obtain its gradient function
	grad_tanh = grad(tanh)
	# Evaluate the gradient at x = 1.0
	out = grad_tanh(1.0)
	# gradient check
	grad_check = (tanh(1.0001) - tanh(0.9999)) / 0.0002

	print('grad_tanh:', grad_tanh)
	print('grad_tanh(1.0):', out)
	print('grad_check:', grad_check)

eg_intro()
