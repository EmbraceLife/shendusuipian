# L1Loss
Least absolute deviations(L1) and Least square errors(L2)
http://pytorch.org/docs/master/nn.html#l1loss

## 公式
```python
from IPython.display import Math
Math(r'{loss}(x, y)  = \frac{1}{n} \sum |x_i - y_i|')
```
## 公式变形
- 我们要看的是函数的变化状态，所有不需要做求均值
- 两个变量，需要固定一个

```python
Math(r' loss(x,y) = \begin{cases} \frac{1}{n}\sum|x_i-1|, & \text{if $y$ set as 1} \\ \frac{1}{n}\sum|x_i-a|, & \text{if $y$ set as any value a} \end{cases}')
```

## x 与 loss 的变化关系
- y = 1 的情况
- x 可以从左右两个方向接近target，越接近，loss值就越小
```python
from sympy import *
x = symbols('x') # y: target, yp: prediction
loss = abs(x-1) # 忽略求均值的计算，因为我们关注的是动态变化
pprint(loss)
plot(loss, xlim=(-1,3), ylim=(0,2))
```

## gradients的智慧
- input > target, gradients帮助input变小
- input < target, gradients帮助input变大
- 变大变小的公式是统一的： input_new = input - lr*grad, 这里体现了gradients的智力

```python
import torch
import torch.nn as nn
import torch.autograd as autograd
loss = nn.L1Loss()
input = autograd.Variable(torch.randn(3, 5), requires_grad=True)
target = autograd.Variable(torch.randn(3, 5))
output = loss(input, target)
output.backward()
input.grad
```
