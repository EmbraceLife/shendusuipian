#####################
# local functions

g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()

outer()
# no way outer.inner()

# useful for one-off functions

####################
# return local functions
def enclosing():
    def local_func():
        print("I am local function")
    return local_func
lf = enclosing()
lf()

#####################
# closure to save variables from above
g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    return inner

inner= outer()
inner()
inner.__closure__
def raise_to(exp):
    def raise_to_exp(x):
        print(locals())
        return pow(x, exp)
    return raise_to_exp
square = raise_to(2.0)
square
square.__closure__
# refer to 2 int
square(5)

#####################
message = 'global'
def enclosing():

    message = 'enclosing'
    def local():
        global message # refer to "global" not "enclosing"
        print('1st:', message)
        message = "local"
    print("enclosing message: ", message)
    local()
    print("enclosing message: ", message)

print('global message:', message)
enclosing()
print('global message:', message)

#####################
message = 'global'
def enclosing():

    message = 'enclosing'
    def local():
        nonlocal message # refer to "enclosing", not 'global'
        print('1st:', message)
        message = "local"
    print("enclosing message: ", message)
    local()
    print("enclosing message: ", message)

print('global message:', message)
enclosing()
print('global message:', message)
