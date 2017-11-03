def hello():
    "print a well-known message"
    print('hello world')

hello()
hello.__doc__
help(hello)
hello.__name__

#################

def noop(f):
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    "print a well-known message"
    print('hello world')

hello()
hello.__doc__
help(hello)
hello.__name__


#################

def noop(f):
    def noop_wrapper():
        return f()
    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper

@noop
def hello():
    "print a well-known message"
    print('hello world')

hello()
hello.__doc__
help(hello)
hello.__name__

#################
import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    "print a well-known message"
    print('hello world')

hello()
hello.__doc__
help(hello)
hello.__name__

##########################
# a popular use of decorator
# make sure the func args second args is non-negative
def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index]<0:
                raise ValueError('Argument {} must be non-negative.'.format(index))
            return f(*args)
        return wrap
    return validator

@check_non_negative(1) # decorator function is not check_non_negative but its output function validator
def create_list(value, size):
    return [value] * size

create_list('a', 3)
create_list("a", -3)
