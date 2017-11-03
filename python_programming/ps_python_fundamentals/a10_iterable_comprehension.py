# list comprehension

pythons = "python3 is the way to go and python can do almost everything I need with a programming language"
pylst = pythons.split()
pylst
[len(word) for word in pylst]
 [x**2 for x in range(5)]
# set comprehension
{x**2 for x in [1,2,2,3,3,4,4]}

# dict comprehension
dllib = {'kr':"keras", 'tf':"tensorflow", 'pt':"pytorch"}
[key+" is "+value for key, value in dllib.items()]
# key must be unique, immutable
pylst = ['py', 'pybrain', 'keras', 'pprint']
{x[0:2]:x for x in pylst}

# if comprehension
cond = True
[x**2 for x in [1,2,2,3,3,4,4] if cond == True]
# 1st order: for loop
# 2nd order: if
# 3rd order: x**2

#########################
# iterable object and iterator
# iterator = iter(iterable)
# item = next(iterator)

lst = ['py2', 'py3', 'autograd', 'pytorch']
iterator = iter(lst)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)

def handle_StopIteration(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")
handle_StopIteration(lst)
handle_StopIteration(lst)
handle_StopIteration(set())

##################
# generator function
def how_generator():
    yield "py2"
    yield "py3"
    yield "autograd"

g = how_generator()
type(g)
next(g)
next(g)
next(g)
next(g)

# use for loop to avoid StopIteration
for i in how_generator():
    print(i)

h = how_generator()
g = how_generator()
id(h)
id(g)
next(g)
next(h)
next(g)
next(g)
next(h)

def how_generator():
    print("about to output py2")
    yield "py2"
    yield "py3"
    yield "autograd"
    print("about to StopIteration")
g = how_generator()
next(g)
next(g)
next(g)
next(g)

############################
# stateful generators
def take(count, iterable):
    print("Inside take: to yield a single item")
    counter = 0
    for item in iterable:
        if counter == count:
            print("counter == count now, no yield anymore")
            return
        counter+=1
        print("Inside take: let's yield %d"%item)
        yield item

def run_take():
    items = [2,4,6,8,10]
    # for loop take()从哪里开始循环？
    for item in take(3, items):
        print(item)

run_take()

def distinct(iterable):
    print("start distict()")
    seen = set()
    # run_distinct's for loop want from here
    for item in iterable:
        print("Inside distinct: we got %d" % item)
        print("seen has ", seen)
        if item in seen:
            print("seen before, no yield")
            continue
        print("Inside distinct: let's yield %d"%item)
        yield item
        seen.add(item)
def run_distinct():
    items = [5,7,7,6,9,9]
    for item in distinct(items):
        print("Inside run_distinct: print %d" % item)

run_distinct()

def run_pipline():
    items = [3,6,6,2,1,1]
    for item in take(3, distinct(items)):
        print("Inside run_pipline: print %d" % item)

run_pipline()

def lucas():
    yield 2
    a = 2
    b = 1
    while b < 10: # if while True, run till end of memory
        yield b
        a, b = b, a+b
for x in lucas():
    print(x)

########################
# generator comprehension
[x**2 for x in range(1,5)]
(x**2 for x in range(1,5))
gen_comp = (x**2 for x in range(1,5))
for i in gen_comp:
    print(i)
# why better than list comprehension?
gen_comp = (x**2 for x in range(1,5))
list(gen_comp) # take a lot of memory
list(gen_comp)
# save a lot of memory
# generator will exhaust

sum([x**2 for x in range(1,5)])
sum(x**2 for x in range(1,5))
import inspect
inspect.getdoc(sum)

############################
# from itertools import islice, count, chain， too advanced for me at the moment
# zip： 已经学过
# any 只要有一个满足条件就行；
any ( [ True ] )
any ( [ True, True, True ] )
any ( [ True, True, False ] )
z = [ 10, 20, 30 ]
any ( [ x > 10 for x in z ] )
any ( [ x > 50 for x in z ] )
any( [ 0, 0, "0", 0 ] )
any ( [ 0, 0, "", 0 ] )
any ( [ [ ], ( ), { }, None, 0 ] )
any ( [ [0], ( ), { }, None, 0 ] )
# all 需要全部满足条件才行；
all ( [ True, True, True ] )
all ( [ True, True, False ] )
z = [ 10, 20, 30 ]
all ( [ x>10 for x in z ] )
all ( [ x>5 for x in z ] )
all ( [ " ", "0", [0], "None" ] ) # space is a character, the string is not empty
all( [ "", "0", [0], "None" ] )
all ( [] )
any ( [] )
all([0])
all([[0]])
all([])
any([])
any([0])
any([[0]])
