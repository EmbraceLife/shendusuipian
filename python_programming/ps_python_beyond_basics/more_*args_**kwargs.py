#######################
def add(**kwargs):
    print("**kwargs: ", kwargs)
    print(tuple(kwargs.values()))
    return sum(tuple(kwargs.values()))
def func_func(add, *args, **kwargs):
    return(add(**kwargs))
func_func(add, num1=1,num2=2,n1=5,n2=6)


def add(*args, **kwargs):
    print("*args: ", args)
    print("**kwargs: ", kwargs)
    print(tuple(kwargs.values()))
    return sum(args+tuple(kwargs.values()))
def func_func(add, *args, **kwargs):
    return(add(*args, **kwargs))
func_func(add, 1,2,n1=5,n2=6)



def add(num1, num2, **kwargs):
    print("**kwargs: ", kwargs)
    print(tuple(kwargs.values()))
    return sum((num1, num2)+tuple(kwargs.values()))
def func_func(add, n1, n2,   **kwargs):
    return(add(n1, n2, **kwargs))
func_func(add, n1=1,n2=2,  n11=5,n12=6)


def add(num1, num2):
    return sum((num1, num2))
def func_func(add, **kwargs):
    return(add(num1=kwargs["num1"], num2=kwargs['num2']))
func_func(add, num1=1,num2=2)

def add(num1, num2):
    return sum((num1, num2))
def func_func(add, **kwargs):
    return(add(kwargs["n1"], kwargs['n2']))
func_func(add, n1=1,n2=2)


def add(num1, num2):
    return sum((num1, num2))
def func_func(add, **kwargs):
    return(add(**kwargs))
func_func(add, num1=1,num2=2)


def add(num1, num2):
    return sum((num1, num2))
def func_func(add, **kwargs):
    return(add(**kwargs))
func_func(add, n1=1,n2=2)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
z = [a,b,c]
z
for i in zip(*z):
    print(i)
for i in zip(a, b, c):
    print(i)
