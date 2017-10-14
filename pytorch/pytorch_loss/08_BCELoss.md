
# BCELoss (Binary Cross Entropy Loss)
http://pytorch.org/docs/master/nn.html#bceloss

## pytorch doc 是如何描述的？
```python
from IPython.display import Math
Math(r'loss(o, t) = - \frac{1}{n} \sum_i (t[i] \log(o[i]) + (1 - t[i]) \log(1 - o[i]))')
```

## 吴恩达课程里说可以这样理解
```python
Math(r'  f(n) = \begin{cases} - \frac{1}{n} \sum_i (\log(1 - o[i]),  & \text{if $t[i]$ is 0} \\ - \frac{1}{n} \sum_i (t[i] \log(o[i])), & \text{if $t[i]$ is 1} \end{cases}')
```

## 把图形画出来，增进理解
当target=1时，prediction越大，损失值越小；
当target=0时，prediction越小，损失值越小；
```python
from sympy import *
y, yp = symbols('y yp') # y: target, yp: prediction
loss = -(y*log(yp)+(1-y)*log(1-yp)) # 忽略求均值的计算，因为我们关注的是动态变化
pprint(loss)
lines = plot(-log(yp), -log(1-yp), show=False)
lines[0].line_color = 'red'
lines[1].line_color = 'cyan'
lines.show()
```
