len("hello")

"love" + "python"

" ".join(["python3", "is", "better"])

" ".join(["python3", "is", "better"]).split(" ")

"unforgetable".partition("forget")

departure, seperator, arrival = "London:Edinburgh".partition(":")
departure
seperator
arrival

p1, _, p2 = "python3vspython2".partition("vs")
p1
p2
_

"use {what_lang} for {what_platform}".format(what_lang="python3", what_platform="joinquant")

help(str)

######################
# arithmetic progression of integers

range(5)
list(range(5))
for i in range(5):
    print(i)

range(5,10)
list(range(5,10))
list(range(0, 10, 2)) # must use 3 args

# use iterations over objects rather than always use idx out of range

# need index for objects
t = [2,5,3,4,6,7,93,4]
for idx, value in enumerate(t):
    print("idx: %d, value: %s" % (idx, value))

############################
# heterogeneous mutable sequence
"python is good for data science".split()

s = "python is good for data science".split()
s[-1]
s[0]
s[5]
s[-6]
s[1:4]
s[1:-1]
s[1:]
s[:3]
copyList = s[:]
copyList == s
copyList is s
id(copyList)
id(s)
copyList.append("more")
copyList
s
copyList == s

# 3 ways to copy a list with difference reference address
lst = [1,2,3]
copyList1 = lst[:]
copyList2 = lst.copy()
copyList3 = list(lst)
copyList1 == copyList2
copyList1 is copyList2

###########################
# shallow copy
a = [[1,3], [5,8]]
b = a[:]
a == b
a is b
id(a)
id(b)
id(a[1])
id(b[1])
id(a[0])
id(b[0])

a[0]
a[0]=[-1, -3] # object | address is changed
b[0]
a == b
id(a[0])
id(b[0])

a[1]
b[1]
a[1].append(12) # same object address
a[1] == b[1]
b[1]
id(a[1])
id(b[1])

# list repetition
a = [1,2]
id(a)
a*3
a
id(a)

[0]*9
[[-1,1]]*2
s = [[-1,1]]*2
id(s)
id(s[0])
id(s[1])
s[1].append(3)
s[1]
s

# finding elements
w = "python is good for data science python"
w.index("data")
w[19]
w.count("good")
w.count("a")
w.count("py")
"good" in w
"python2" not in w

# remove elements
w1 = w.split()
del w1[-1]
w1
del w1[w1.index('for')]
w1
w1.remove("data")
w1
w1.insert(0, "I")
w1

w1+w1
w1+=w1
w1.extend([1,2,3])
w1

# reverse, sort list
w1.reverse()
w1
w2 = [1,2,3,4,43,25,12]
w2.sort()
w2
w2.sort(reverse=True)
w2

# sort by key
w3 = "python is great".split()
w3.sort(key=len, reverse=True)
w3

# not inplace effect
w3 = "python is great".split()
x1 = sorted(w3)
w3
x1

w4 = [2,4,3,6,8]
x2 = reversed(w4)
w4
x2
list(x2)
