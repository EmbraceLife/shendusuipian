class Callable:
    def __init__(self):
        print("creating a callable object now")

    def __call__(self):
        print("now this object can act like a func")

c = Callable()
c()
type(c)
# test whether it is callable
callable(c)
type
callable(tuple)
callable(list)
callable(int)
callable(str)
callable((2,3))
callable("hello")
