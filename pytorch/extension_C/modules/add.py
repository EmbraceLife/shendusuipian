# modules/add.py
from torch.nn import Module
from functions.add import MyAddFunction

class MyAddModule(Module):
    def forward(self, input1, input2):
        return MyAddFunction()(input1, input2)
