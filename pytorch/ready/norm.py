
######## torch.norm # take normalizaiton L1, L2 ################
import numpy as np
import torch
from torch.autograd import Variable
a = (torch.ones(3,2)*2)
torch.norm(a)
torch.norm(a, p=2)
torch.norm(a, p=2, dim=1)
torch.norm(a, p=2, dim=0)#, keepdim=True)
torch.norm(a, p=2, dim=0, keepdim=True)
np.sqrt(24)
