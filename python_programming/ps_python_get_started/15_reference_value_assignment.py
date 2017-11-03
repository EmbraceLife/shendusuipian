##############################
# 如何用函数改变global variable 的值
a, b, c = (1, 2, 3)

def test():     # no local variable is defined here
    print("a:", a)    # a is global variable
    print("b:", b)    # b is global variable
    print("c:", c)    # c is global variable
    d = a+1           # local variable d is created and assigned
    print("d:",d)     # won't exist outside
    # a = a+1           # error: local variable a referenced before assignment
test()
a

###############################
# 函数赋值
def test():     # no local variable is defined here
    print("a:", a)    # a is global variable
    print("b:", b)    # b is global variable
    print("c:", c)    # c is global variable
    d = a+1     # local variable d is created and assigned
    print("d:",d)    # won't exist outside
    # a = a+1     # error: local variable a referenced before assignment
    return d
a = test()
a

#################################
# 函数不赋值，但要求global variable 是 mutable objects: list, dict
A = {"a": 1, "b": 2, "c":3}

def test():     # no local variable is defined here
    print("a:", A["a"])    # a is global variable
    print("b:", A["b"])    # b is global variable
    print("c:", A["c"])    # c is global variable
    A["a"] = A["a"]+1     # local variable d is created and assigned
    # a = a+1     # error: local variable a referenced before assignment
test()
A

##############################
# 如何用函数改变global variable 的值
a, b, c = (1, 2, 3)

def test():     # no local variable is defined here
    global a          # 让下面的local variable a 变成 global
    print("a:", a)    # a is global variable
    print("b:", b)    # b is global variable
    print("c:", c)    # c is global variable

    a = a+1     # local variable d is created and assigned
    # a = a+1     # error: local variable a referenced before assignment
test()
a
