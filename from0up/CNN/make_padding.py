"""
why padding to the same?
1. add padding to keep "same" width, height for deep networks
2. don't lose information

help(np.pad)
"""
import numpy as np


def m_images_pad(X, pad):
    """
    Pad with zeros all images of the dataset X. The padding is applied to the height and width of an image, as illustrated in image above

    Argument:
    X -- python numpy array of shape (m, n_H, n_W, n_C) representing a batch of m images
    pad -- integer, amount of padding around each image on vertical and horizontal dimensions

    Returns:
    X_pad -- padded image of shape (m, n_H + 2*pad, n_W + 2*pad, n_C)
    """

    ### START CODE HERE ### (≈ 1 line)
    X_pad = np.pad(X, ((0, 0), (pad,pad), (pad,pad), (0,0)), 'constant')
    ### END CODE HERE ###

    return X_pad

if __name__ == "__main__":


    ## part1 - Zero-Padding
    import numpy as np
    import matplotlib.pyplot as plt
    # python make_padding report syntax error, no # after % line
    %matplotlib inline
    plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'

    # %load_ext autoreload
    # %autoreload 2

    np.random.seed(1)
    from IPython.display import Image
    import matplotlib.pyplot as plt
    Image(url="http://r.photo.store.qq.com/psb?/V119hAgO3es3Ib/.1LGB0hH5ql14.eWrYiJcd.E6pAEoTko663CQlXCUAs!/r/dOIAAAAAAAAA", width=500) # (3 channels, RGB) with a padding of 2


    np.random.seed(1)
    x = np.random.randn(4, 3, 3, 2)
    x_pad = m_images_pad(x, 2)
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
