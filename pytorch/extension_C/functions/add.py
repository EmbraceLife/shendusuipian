# functions/add.py
import torch
from torch.autograd import Function
from _ext import my_lib


class MyAddFunction(Function):
    def forward(self, input1, input2):
        output = torch.FloatTensor()
        my_lib.my_lib_add_forward(input1, input2, output)
        return output

    def backward(self, grad_output):
        grad_input = torch.FloatTensor()
        my_lib.my_lib_add_backward(grad_output, grad_input)
        return grad_input
