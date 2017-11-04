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


#######################################
# standardize m_images, image values range from [0, 1]
m_images = m_images/255


#######################################
# flatten an image: 让 (m, row, col) 变成 (m, row*col)
m_images = m_images.reshape((m_images.shape[0], -1))
m_images.shape


#######################################
# 用ipython打开展示图片
import os
from IPython.display import display, Image
help(Image)
names = [f for f in os.listdir('./images/') if f.startswith('Log')]
for name in names:
    display(Image("./images/"+name, width=600))
Image(url="http://r.photo.store.qq.com/psb?/V119hAgO2ped1p/PTV2rkdWT*dMcpGd8kSknEG1Z2bqCOwnQQpNccTCnEI!/r/dE0AAAAAAAAA", width=600)

#######################################
# 如何用ipython写数学公式
from IPython.display import Math
Math(r'z^{(i)} = w^T x^{(i)} + b \tag{1}')
Math(r'\hat{y}^{(i)} = a^{(i)} = sigmoid(z^{(i)})\tag{2}')
Math(r" \mathcal{L}(a^{(i)}, y^{(i)}) =  - y^{(i)}  \log(a^{(i)}) - (1-y^{(i)} )  \log(1-a^{(i)})\tag{3}")
Math(r' J = \frac{1}{m} \sum_{i=1}^m \mathcal{L}(a^{(i)}, y^{(i)})\tag{6}')

#######################################
# 如何构建W初始化(归0的初始化)？
def initialize_w_b(row, col):
    """创建W，b, 值全部为0
    Args:
        row: weights.shape[0]
        col: weights.shape[1]
    Returns:
        w: weights,
        b: bias

    """
    w = np.zeros((row, col))
    b = np.zeros(1)

    assert(w.shape == (row, col))
    assert(isinstance(b, np.ndarray) or isinstance(b, int))

    return w, b

row = m_images.shape[-1] # 要求weights.shape[0] == input_features的数量
col = 1 # 隐藏层只有一个神经元
w, b = initialize_w_b(row, col)


#######################################
# 如何构建Linear函数？
def linear(X, w, b):
    """做linear combination 计算
    Args:
        X: input array or tensor
        w: weight array or tensor
        b: bias array or scalar
    Return:
        z: scalar or array
    """
    # np.dot: 要求 X.shape[-1] == w.shape[-2] must be true
    z = np.dot(X, w) + b
    return z

help(np.dot)

m_images.shape
w.shape
b.shape
z = linear(m_images, w, b)
z

#######################################
# 如何构建sigmoid函数？
Math(r'sigmoid( w^T x + b) = \frac{1}{1 + e^{-(w^T x + b)}}')

# import sympy as sp
# z = sp.symbols('z')
# s = 1/(1+sp.exp(-z))
# sp.plot(s, (z, -5, 5))
# help(sp.plot)

# def sigmoid(z):
#     s = 1/(1+np.exp(-z))
#     return s

def sigmoid(x):
    return 0.5*(np.tanh(x) + 1)

s = sigmoid(z)
s


##################################
# 创建损失函数loss function
def logloss(s, y, m):
    ll = -(1/m)*np.sum(y*np.log(s)+(1-y)*np.log(1-s))
    return ll

m = m_images.shape[0]
y = m_labels
loss = logloss(s, y, m)
loss


##################################
# 创建grad函数
import autograd.numpy as np   # Thinly-wrapped version of Numpy
from autograd import grad
loss_grad = grad(logloss)
loss_grad(s, y, m)
w.shape
help(grad)


def logloss(w, b, m_images, y):
    z = linear(m_images, w, b)
    s = sigmoid(z)
    ll = -(1/m)*np.sum(y*np.log(s)+(1-y)*np.log(1-s))
    return ll

y = m_labels
loss = logloss(w,b,m_images, y)
loss

grad_loss = grad(logloss)
grad_loss(w,b,m_images,y)


##################################
# 创建optimizer函数
def optimizer(w, b, m_images, m_labels, learning_rate, epochs):

    for i in range(epochs):
        loss = logloss(w,b,m_images, m_labels)
        print("loss: ", loss)
        grad_loss = grad(logloss)
        grads_w = grad_loss(w,b,m_images,m_labels)
        w -= learning_rate*grads_w

w, b = initialize_w_b(36,1)
optimizer(w, b, m_images, m_labels, 0.01, 5)
