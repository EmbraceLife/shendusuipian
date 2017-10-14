# MSELoss (Mean Squared Error Loss)
http://pytorch.org/docs/master/nn.html#mseloss

## 公式
```python
from IPython.display import Math
Math(r'loss(x, y) = \frac{1}{n} \sum |x - y|^2')
```

## 公式变形
- 我们要看的是函数的变化状态，所有不需要做求均值
- 两个变量，需要固定一个

```python
Math(r' loss(x,y) = \begin{cases} \frac{1}{n} \sum |x - 1|^2, & \text{if $y$ set as 1} \\ \frac{1}{n} \sum |x - a|^2, & \text{if $y$ set as any value a} \end{cases}')
```

## 函数作图
- y = 1 的情况
- x 可以从左右两个方向接近target，越接近，loss值就越小
```python
from sympy import *
x = symbols('x') # y: target, yp: prediction
loss = (abs(x-1))**2 # 忽略求均值的计算，因为我们关注的是动态变化
pprint(loss)
plot(loss, xlim=(-1,3), ylim=(0,2))
```

## L1Loss vs MSELoss
- 对比图可以看出两者的差异
- 何时用L1Loss or MSELoss, 取决于他们是否能更真实的描述当前面对现实情况

```python
from sympy import *
x = symbols('x') # y: target, yp: prediction
L1loss = abs(x-1)
MSEloss = (abs(x-1))**2 # 忽略求均值的计算，因为我们关注的是动态变化
pprint(L1loss)
pprint(MSEloss)
lines = plot(L1loss, MSEloss, xlim=(-1,3), ylim=(0,2), show=False)
lines[0].line_color = 'gray'
lines[1].line_color = 'blue'
lines.show()

```
