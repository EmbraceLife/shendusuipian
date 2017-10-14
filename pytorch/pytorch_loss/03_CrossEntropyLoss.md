# CrossEntropyLoss
http://pytorch.org/docs/master/nn.html#crossentropyloss

## logsoftmax vs softmax 直观区别
```python
import torch
import torch.nn as nn
import torch.autograd as autograd
m = nn.LogSoftmax()
input = autograd.Variable(torch.randn(2, 3))
print(input)
print(m(input))
print(nn.functional.softmax(input))
```

## 公式
```python
from IPython.display import Math
Math(r'loss(x, class) = -\log(e^{x[class]}/\sum(e^{x[j]})) = -x[class]+\log(\sum_j(e^{x[j]}))')
import sympy as sp
x = sp.symbols('x')
lines = plot(sp.log(x), sp.exp(x), xlim=(-2,2), ylim=(-2,2), show=False)
lines[0].line_color = 'gray'
lines[1].line_color = 'blue'
lines.title = "gray=log(x), blue=exp(x)"
lines.show()
```

## 案例
```python
import torch
import torch.nn as nn
import torch.autograd as autograd
loss = nn.CrossEntropyLoss()

# 这里的input,实际上就是我们的模型prediction, 3个样本，5个class
input = autograd.Variable(torch.randn(3, 5), requires_grad=True)
input.grad
# target: 每个样本所对应的 正确的class
target = autograd.Variable(torch.LongTensor(3).random_(5))
output = loss(input, target)
output.backward()
input.grad

```

## 从案例回到公式
- 从案例发散：
	- input_new = input - lr*input_grad
	- doc step: http://pytorch.org/docs/master/_modules/torch/optim/sgd.html#SGD
	- `input` 也就是 `prediction` 如果预测正确，那么正确的 input[class]会被放大
	- 而其他的input[-class]会被变小
- 公式也是这个意思吗？

```python
import sympy as sp
x1,x2,x3,x4,x5 = sp.symbols('x1 x2 x3 x4 x5')
loss = -x5 + sp.log(sp.exp(x1)+sp.exp(x2)+sp.exp(x3)+sp.exp(x4)+sp.exp(x5))
loss.diff(x5)
loss.diff(x5).evalf(subs={x5:0.5422, x2:1.286, x3:0.2446, x4:0.5300, x1:0.2103})
loss.diff(x3).evalf(subs={x5:0.5422, x2:1.286, x3:0.2446, x4:0.5300, x1:0.2103})
loss.diff(x1).evalf(subs={x5:0.5422, x2:1.286, x3:0.2446, x4:0.5300, x1:0.2103})

loss = -x3 + sp.log(sp.exp(x1)+sp.exp(x2)+sp.exp(x3)+sp.exp(x4)+sp.exp(x5))
loss.diff(x3).evalf(subs={x1:1.4388, x2:1.0786, x3:-1.3075, x4:0.6059, x5:-0.8175})
loss.diff(x2).evalf(subs={x1:1.4388, x2:1.0786, x3:-1.3075, x4:0.6059, x5:-0.8175})
loss.diff(x4).evalf(subs={x1:1.4388, x2:1.0786, x3:-1.3075, x4:0.6059, x5:-0.8175})
# Variable containing:
#  1.2860  0.2446  0.5300  0.2103  0.5422
#  1.4388  1.0786 -1.3075  0.6059 -0.8175
# -1.3135  1.0184 -0.2270 -0.2106  1.1886
# [torch.FloatTensor of size 3x5]
```
