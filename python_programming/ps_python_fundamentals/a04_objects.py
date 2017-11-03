id(10)
a = 10
id(a)
id(2)
id(a+2)
id(12)
b = a+2
id(b)
a = b
id(a)

#########################
id([1,2,3])
c = [1,2,3]
id(c)
d = c
id(d)
# list is mutable
c.append(4)
c
id(c)
id(d)
d

x = [1,2,3]
y = [1,2,3]
id(x)
id(y)
# value difference
x == y
# identity or address difference
x is y

############################
x = [1,2,3]
id(x)
def add_1(m):
    print("before: local m: ", m, " local m address: ", id(m))
    d = list(map(lambda x: x+1, m)) # initialized a new list
    print("after, local m: ", m, " local m address: ", id(m))
    print("after, local d: ", d, " local d address: ", id(d))


add_1(x)
x
id(x)


############################################################
x = [1,2,3]
id(x)
def add_1(m):
    print("before: local m: ", m, " local m address: ", id(m))
    m = list(map(lambda x: x+1, m)) # initialized a new list
    print("after, local m: ", m, " local m address: ", id(m))


add_1(x)
x
id(x)


############################################################
x = [1,2,3]
id(x)
def add_1(m):
    print("before: local m: ", m, " local m address: ", id(m))
    for i in range(len(m)):
        m[i] = m[i]+1 # 赋值的一瞬间，会产生一个新的local variable 和 新的地址
    print("after, local m: ", m, " local m address: ", id(m))


add_1(x)
x
id(x)
