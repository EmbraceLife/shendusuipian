def func_args(positional_arg, named_arg, default_arg = []):
    print("positional_arg: ", positional_arg)
    print("named_arg: ", named_arg)
    print("default_arg: ", default_arg)

func_args(3, 5)

func_args(3, 5, [7])

func_args(3, named_arg=5)

# func_args(3, named_arg=5, [7])
# SyntaxError: positional argument follows keyword argument

# func_args(3, [7], named_arg=5)
# TypeError: func_args() got multiple values for argument 'named_arg'

func_args(3, named_arg=5, default_arg=[7])

####################################
def func_args(positional_arg, named_arg, default_arg = [7]):
    print("positional_arg: ", positional_arg)
    print("named_arg: ", named_arg)
    print("default_arg: ", default_arg)
    default_arg = default_arg.append(7)

func_args(3, 5)
func_args(3,5)
func_args(3,5)

####################################
# problem why: default arg will only run once
# solution: use immutable objects, integer, string, None
# don't use mutable objects like list and dict
def func_args(positional_arg, named_arg, default_arg = 7):
    print("positional_arg: ", positional_arg)
    print("named_arg: ", named_arg)
    print("default_arg: ", default_arg)
    lst = []
    default_arg = lst.append(default_arg)

func_args(3,5)
func_args(3,5)
func_args(3,5)
