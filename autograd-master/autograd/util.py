import sys

def subvals(x, ivs):
    """
    Args:
        ivs: 是enumerate object
        x: 是一个list like object
    logic:
        将x变成一个list, 将ivs的值按顺序放入x里，再将x变成tuple
    Return:
        返回一个tuple
    """
    x_ = list(x)
    for i, v in ivs:
        x_[i] = v # ivs can't be a dict
    return tuple(x_)

def subval(x, i, v):
    """
    Args:
        x: 是一个list like object
        i: scalar, index
        v: scalar, 对应index的值
    logic:
        将x变成一个list, 用i作为index, v 作为value，放入x里
    Return:
        返回一个tuple
    """
    x_ = list(x)
    x_[i] = v
    return tuple(x_)

if sys.version_info >= (3,):
    def func(f): return f
else:
    def func(f): return f.im_func

################## experiment
# x = [1,2,3]
# list(x)
# ivs = enumerate([1,2,3])
# for i, v in ivs: print(i, v)
# subvals(x, ivs)

# -------------------- deprecation warnings -----------------------

import warnings
deprecation_msg = """
The quick_grad_check function is deprecated. See the update guide:
https://github.com/HIPS/autograd/blob/master/docs/updateguide.md"""

def quick_grad_check(fun, arg0, extra_args=(), kwargs={}, verbose=True,
                     eps=1e-4, rtol=1e-4, atol=1e-6, rs=None):
    warnings.warn(deprecation_msg)
    from autograd.test_util import check_grads
    fun_ = lambda arg0: fun(arg0, *extra_args, **kwargs)
    check_grads(fun_, modes=['rev'], order=1)(arg0)
