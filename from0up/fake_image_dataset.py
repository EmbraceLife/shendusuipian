import autograd.numpy as np
from autograd import grad
from sklearn.preprocessing import minmax_scale

###################################################
# create fake image data

### create normal distribution random matrix
help(np.random.randn) # mean = 0, std = 1, normal distribution
help(np.random.randint)
### transform np.array to min max range
import sklearn
help(sklearn) # 查阅所有packages, modules
from sklearn.preprocessing import minmax_scale
help(minmax_scale)

### actual codes
rand = np.random.randn(6,6)
image = minmax_scale(rand, feature_range=(0, 255))
image.max()
image.min()

### 构建函数来create fake images
def fake_images(m, row, col):
    """ 创建m个单色images，每张图片的pixel值的分布是正态分布，值被强制规范在0-225之间
    Args:
        m: 图片的张数, int
        row: 图片长, int
        col: 图片宽, int
    Returns:
        m_images: np.array shape (m, row, col)
    """
    # 构建random normal distribution, shape (m, row, col), mean=0, std=1
    rand = np.random.randn(m, row, col)
    m_images = []

    # 让 rand 的值都在 (0, 225) 之间
    for i in range(rand.shape[0]): # 对每一个image: np.array (row, col) 做一下操作
        images = minmax_scale(rand[i], feature_range=(0, 255)) # minmax_scale 只接受 2d np.array (row, col)
        m_images.append(images)
    m_images = np.array(m_images) #从list 到 np.array
    return m_images

m_images = fake_images(5, 6, 6)

m_labels = np.random.randint(0,2,5)# [low=0, high=2), size=5
