def print_name(name):
    return name
print_name("深度碎片")

def print_name(name):
    return ascii(name)
print_name("深度碎片")

# decorator: input f, output wrap,都是func
def escape_unicode(f):
    def wrap(*args, **kwargs):
        print("*args: ", args)
        print("**kwargs: ", kwargs)
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def print_name(name):
    return name

print_name("深度碎片")
print_name(name="深度碎片")

#################
# Class as decorator: 输入func -> __init__(f); 输出 func -> __call__()
class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count+=1
        return self.f(*args, **kwargs)

@CallCount # 相当于callcount object
def hello(name):
    print("hello, {}".format(name))

hello("python")
hello.count
hello.f
hello.__class__
###################
# class instance as decorator
class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self, f): # input arg: f; output: wrap func
        def wrap(*args, **kwargs):
            print("*args: ", args)
            print("**kwargs: ", kwargs)
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]
l = [1,2,3]
rotate_list(l)
rotate_list(l)
tracer.enabled = False
rotate_list(l=l)
rotate_list.__class__
dir(rotate_list)
#########################
# multiple decorators, from bottom up

class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self, f):
        def wrap(*args, **kwargs):
            print("tracer: *args: ", args)
            print("tracer: **kwargs: ", kwargs)
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap
tracer = Trace()

def escape_unicode(f):
    def wrap(*args, **kwargs):
        print("escape: *args: ", args)
        print("escape: **kwargs: ", kwargs)
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@tracer
@escape_unicode
def multiple_deco(name):
    return name

multiple_deco("python")
multiple_deco("python,真棒")
tracer.enabled = False
multiple_deco("python,好样的")

@escape_unicode
@tracer
def multiple_deco(name):
    return name
tracer.enabled = True
multiple_deco("python")

##########################
# decorators for class method
class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name+self.suffix
island = IslandMaker('python')
island.make_island("py3.6")
