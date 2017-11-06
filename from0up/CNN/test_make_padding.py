import make_padding
dir(make_padding)
help(make_padding)



## 设置作图参数
import numpy as np
import matplotlib.pyplot as plt

# % 只能用于jupyter style; 设置 inline plotting
%matplotlib inline

plt.rcParams['figure.figsize'] = (5.0, 4.0) # 设置figure_size尺寸
plt.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
plt.rcParams['image.cmap'] = 'gray' # 设置 颜色 style

# %load_ext autoreload
# %autoreload 2

from IPython.display import Image # 展示图片online
import matplotlib.pyplot as plt
Image(url="http://r.photo.store.qq.com/psb?/V119hAgO3es3Ib/.1LGB0hH5ql14.eWrYiJcd.E6pAEoTko663CQlXCUAs!/r/dOIAAAAAAAAA", width=500) # (3 channels, RGB) with a padding of 2


np.random.seed(1)
x = np.random.randn(4, 3, 3, 2)
x_pad = make_padding.m_images_pad(x, 2)
print ("x.shape =", x.shape)
print ("x_pad.shape =", x_pad.shape)
print ("x[1,1] =", x[1,1])
print ("x_pad[1,1] =", x_pad[1,1]) # 第二个sample image, 2nd width pixel 上的纵截面(height, channels)

# 有时候必须一起运行，才行
fig, axarr = plt.subplots(1, 2) # 1行，2图
axarr[0].set_title('x') # 第一图的title
axarr[0].imshow(x[0,:,:,0]) # 在第一图的位置，画第一个样本的第一个channel
axarr[1].set_title('x_pad') # 第二图的title
axarr[1].imshow(x_pad[0,:,:,0]) # 在第二图的位置，画第一个样本的第一个channel
