def what(*args):
    print(args)
    print(type(args))

what(1)
what(1,2)

def add(*args):
    return sum(args)

add(1)
add(1,2,4)

def add(*args):
    print("what is args? type(args) = {}, {}".format(type(args), args))
    iterator = iter(args)
    print("sum with iterable: sum(args) = %i"%sum(args))
    print("sum with iterator: sum(iterator) = %i"%sum(iterator))


add(1)
add(1,2,3)

def add(num, *args, **kwargs):
    print("num is %i"%num)
    print("*args is type: {}, print as {}".format(type(args), args))
    print("**kwargs is type: {}, print as {}".format(type(kwargs), kwargs))

add(1, 2, 3, num1=4, num2=5)

def add(num, *args, else1, else2, **kwargs):
    print("num is %i"%num)
    print("*args is type: {}, print as {}".format(type(args), args))
    print("else1 is type: {}, print as {}".format(type(else1), else1))
    print("else2 is type: {}, print as {}".format(type(else2), else2))
    print("**kwargs is type: {}, print as {}".format(type(kwargs), kwargs))
add(1, 2, 3, else1=6, else2=7, num1=4, num2=5)

#############
(1,2)+ (3,4)
def add(num1, num2, *args):
    print("num1: ", num1)
    print("num2: ", num2)
    print("*args: ", args)
    return sum((num1, num2)+args)
add(1,2,3,4)
t = (1,2,3,4)
add(t)
add(*t)

def add(num1, num2, *args, **kwargs):
    print("num1: ", num1)
    print("num2: ", num2)
    print("*args: ", args)
    print("**kwargs: ", kwargs)
    print(tuple(kwargs.values()))
    return sum((num1, num2)+args + tuple(kwargs.values()))
add(1,2,3,4,n1=5,n2=6)
t2 = {"num1":1,"num2":2,"a":3,"b":4,"n1":5,"n2":6}
add(**t2)


def add(*args, num1, num2, **kwargs):
    print("num1: ", num1)
    print("num2: ", num2)
    print("*args: ", args)
    print("**kwargs: ", kwargs)
    print(tuple(kwargs.values()))
    return sum((num1, num2)+args + tuple(kwargs.values()))
add(1,2,3,4,n1=5,n2=6)
add(1,2,num1=3,num2=4,n1=5,n2=6)
t2 = {"num1":1,"num2":2,"a":3,"b":4,"n1":5,"n2":6}
add(**t2)
