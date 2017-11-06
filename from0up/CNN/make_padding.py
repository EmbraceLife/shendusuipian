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
