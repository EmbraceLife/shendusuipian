from numbers import Integral
import warnings
import math

import torch
from torch._C import _infer_size
from . import _functions
from .modules import utils
from ._functions.linear import Bilinear # nn._functions
from ._functions.padding import ConstantPadNd
from ._functions.vision import GridSampler, AffineGridGenerator
from ..autograd import _functions as _autograd_functions
from torch.autograd import Variable
from .modules.utils import _single, _pair, _triple

# Convolutions
ConvNd = torch._C._functions.ConvNd
