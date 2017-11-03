# battery included: contains lots of powerful libs inside in standard installation

help() # interactive help

help(math) # check math library

import math
math.factorial(5)

int
float
None
False or True

10
0b10
0o10
0x10

int(3.5)
int("496")
int("10000", 3)
help() # interactive, then search int, q to exit to view here

3e8
1.252e-3
float(7)
float("1.654")
float("nan")
float("inf")
3.1+2

None
a = None
a is None

True
False
True or False
True and False
bool(0)
bool(-34)
bool(3)
bool([])
bool([1,2,3])
bool("")
bool(" ")
bool("str")
bool("False")
bool("True")

"str" == "str"
3 != 2
3 >= 2

if True:
    print("yes, true")

if False:
    print("no!")

if bool("eggs"):
    print("yes")

3 % 8
11 // 7
14 // 7
11 % 7
14 % 7

# ctrl + c interupt execution

########################
# collections
str  # immutable, '', ""
byte # immutable, b'data', b"data"
# str to byte
data = chinese_string.encode("utf-8")
list # mutable sequences of objects
dict # mutable object

r'' # for double \\
s = str("123")
s[0]
s = "tencent"
s.capitalize()

for index in iterable_object:
    print(index)

# use of with to prevent memory leak
from urllib.request import urlopen
with urlopen("http...") as story:
    story_words = []
    for line in story:
        pass

story_words # can be accessible
