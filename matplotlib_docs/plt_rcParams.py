import numpy as np
import matplotlib.pyplot as plt

def m_images_pad(X, pad):
    X_pad = np.pad(X, ((0, 0), (pad,pad), (pad,pad), (0,0)), 'constant')
    return X_pad
# % 只能用于jupyter style; 设置 inline plotting
%matplotlib inline

plt.rcParams['figure.figsize'] = (8.0, 4.0) # 设置figure_size尺寸
plt.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
plt.rcParams['image.cmap'] = 'gray' # 设置 颜色 style

np.random.seed(1)
x = np.random.randn(4, 3, 3, 2)
x_pad = m_images_pad(x, 2)

# 有时候必须一起运行，才行
fig, axarr = plt.subplots(1, 2) # 1行，2图
axarr[0].set_title('x') # 第一图的title
axarr[0].imshow(x[0,:,:,0]) # 在第一图的位置，画第一个样本的第一个channel
axarr[1].set_title('x_pad') # 第二图的title
axarr[1].imshow(x_pad[0,:,:,0]) # 在第二图的位置，画第一个样本的第一个channel

############################
help(plt.rcParams) # class, dict to store, many methods
plt.rcParams.__dict__
dir(plt.rcParams) # methods for dictionaries
from inspect import getmodule
getmodule(plt.rcParams) # where source code is
plt.rcParams # check all keys and values of the dictionary
print(plt.rcParams)
