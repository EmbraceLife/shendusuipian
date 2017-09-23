# -*- coding: utf-8 -*-
"""
Autograd: automatic differentiation
===================================

Central to all neural networks in PyTorch is the ``autograd`` package.
Let’s first briefly visit this, and we will then go to training our
first neural network.


The ``autograd`` package provides automatic differentiation for all operations
on Tensors. It is a define-by-run framework, which means that your backprop is
defined by how your code is run, and that every single iteration can be
different.

Let us see this in more simple terms with some examples.

Variable
--------

``autograd.Variable`` is the central class of the package. It wraps a
Tensor, and supports nearly all of operations defined on it. Once you
finish your computation you can call ``.backward()`` and have all the
gradients computed automatically.

You can access the raw tensor through the ``.data`` attribute, while the
gradient w.r.t. this variable is accumulated into ``.grad``.

.. figure:: /_static/img/Variable.png
   :alt: Variable

   Variable

There’s one more class which is very important for autograd
implementation - a ``Function``.

``Variable`` and ``Function`` are interconnected and build up an acyclic
graph, that encodes a complete history of computation. Each variable has
a ``.grad_fn`` attribute that references a ``Function`` that has created
the ``Variable`` (except for Variables created by the user - their
``grad_fn is None``).

If you want to compute the derivatives, you can call ``.backward()`` on
a ``Variable``. If ``Variable`` is a scalar (i.e. it holds a one element
data), you don’t need to specify any arguments to ``backward()``,
however if it has more elements, you need to specify a ``grad_output``
argument that is a tensor of matching shape.
"""

import torch
from torch.autograd import Variable

###############################################################
# Create a variable:
x = Variable(torch.ones(2, 2).type(torch.FloatTensor), requires_grad=True)
print(x)

###############################################################
# Do an operation of variable:
y = x + 2
print(y)

###############################################################
# ``y`` was created as a result of an operation, so it has a ``grad_fn``.
print(y.grad_fn)

###############################################################
# Do more operations on y
z = y * y * 3
out = z.mean()
z.grad_fn
out.grad_fn
print(z, out)

###############################################################
# Gradients
# ---------
# let's backprop now
# ``out.backward()`` is equivalent to doing ``out.backward(torch.Tensor([1.0]))``
# out.backward(torch.Tensor([1.0]))
# out.backward(torch.ones(2,2).type(torch.FloatTensor))
out.backward()
# out.backward(torch.ones(2,2).type(torch.FloatTensor))
###############################################################
# print gradients d(out)/dx
#

x.grad

x.grad.data.zero_()

###############################################################
# **Read Later:**
#
# Documentation of ``Variable`` and ``Function`` is at
# http://pytorch.org/docs/autograd
