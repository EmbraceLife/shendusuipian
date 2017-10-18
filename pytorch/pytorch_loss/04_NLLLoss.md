![](/Users/Natsume/Desktop/todayimage/NLLLoss01.png)
![](/Users/Natsume/Desktop/todayimage/NLLLoss02.png)
![](/Users/Natsume/Desktop/todayimage/NLLLoss03.png)


```python
import torch
import torch.nn as nn
import torch.autograd as autograd


m = nn.LogSoftmax()
loss = nn.NLLLoss()
# input is of size nBatch x nClasses = 3 x 5
input = autograd.Variable(torch.randn(3, 5), requires_grad=True)
# each element in target has to have 0 <= value < nclasses
target = autograd.Variable(torch.LongTensor([1, 0, 4]))

# 只对一个样本做logsoftmax处
m(input[0].view(1,5))
output = loss(m(input[0].view(1,5)), target[0])
output.backward()
# backward之后，grad会让对应的param变大，其他的param变小；
# 但是为什么呢？需要看看logsoftmax的特点
input.grad
input
target


```
