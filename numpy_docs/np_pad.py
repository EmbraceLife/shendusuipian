import numpy as np

def m_images_pad(X, pad):
    X_pad = np.pad(X, ((0, 0), (pad,pad), (pad,pad), (0,0)), 'constant')
    return X_pad

np.random.seed(1)
x = np.random.randn(4, 3, 3, 2)
x_pad = m_images_pad(x, 2)
x[1,1]
x_pad[1,1]


help(np.pad)
np.lib.arraypad.__file__
# atom file path: see everything in the module
# def pad is 200 lines long

import numpy.lib.arraypad as pad
dir(pad) # include everything in the module

np.pad # thanks to __all__ = ['pad']
np.lib.pad # thanks to __all__ = ['pad']

from inspect import getsourcelines
getsourcelines(np.pad) # see source code of pad

"""
策略
- 只看当前需要的args, return
- 其他args和用法，需要时在翻出来看
"""
