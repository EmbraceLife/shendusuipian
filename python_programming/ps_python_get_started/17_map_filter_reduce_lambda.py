
## map with lambda and other functions
items = [1, 2, 3, 4, 5]
list(map((lambda x: x **2), items))

list(map(pow, [2, 3, 4], [1, 2, 3]))


## map x, y with operator.add
x = [1,2,3]
y = [4,5,6]
from operator import add
list(map(add, x, y))  # output [5, 7, 9]



# itertools.zip_longest
m = [1,2,3]
n = [1,4,9]
from itertools import zip_longest
for i,j in zip_longest(m,n):
    print(i,j)


# filter, list(range), lambda
list(range(-5,5))
list(filter((lambda x: x < 0), range(-5,5)))



# 取 b 中的值，做filter
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
list(filter(lambda x: x in a, b))  # prints out [2, 3, 5, 7]

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
[x for x in a if x in b] # prints out [2, 3, 5, 7]


# functools.reduce with lambda, x, y 都来自 同一个list
from functools import reduce
reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
reduce( (lambda x, y: x / y), [1, 2, 3, 4] )

import functools
L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
functools.reduce( (lambda x,y:x+y), L)

''.join(L)


import functools, operator
functools.reduce(operator.add, L)
