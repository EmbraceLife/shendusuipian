from autograd.wrap_util import *

from pprint import pprint as pp
locals()
pp(get_doc(subvals))
get_name(subvals)
_wraps = wraps(subvals)
def f(x): pass
f = _wraps(f)
f.__name__
pp(f.__doc__)
def op(x):
    "I am op func"
    pass
argnum = 3
_wraps = wrap_nary_f(subvals, op, argnum)
f = _wraps(f)
f.__name__
pp(f.__doc__)

def unary_operator(x,y,*args, **kwargs): pass
nary_operator = unary_to_nary(unary_operator)

nary_f = nary_operator(subvals, 0)#, 3, 5)
out = nary_f(9)
