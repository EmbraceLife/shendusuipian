# unordered (random), unique immutable keys, mutable values
dct = {"new": "py3", "old":"py2"}

dct1 = [('py2', 80), ('py3',100)]
dct1 = dict(dct1)
dct1
dct1 = dict(py2=80, py3="100")
dct1

# copy dict
dct2 = dct1.copy()
dct2 = dict(dct1)

# extend
dct1.update(dct2)
dct1
dct3 = dict(py4=120)
dct1.update(dct3)
dct1

# iteratable
for key, value in dct1.items():
    print(key, value)
dct1.keys()
dct1.values()

# in or not? for keys only
"py2" in dct1
80 in dct1

del dct1['py2']
dct1

# dct1 is mutable, its values are mutable, not keys
id(dct1)
dct1['py5'] = 200
dct1
id(dct1)
dct1['py3'] = [100, 150]
dct1
id(dct1)

# nice print
from pprint import pprint as pp
pp(dct1)

#######################
# unordered, unique, immutable objects
p = {'py2', 'py3', 32}
p
type(set())
type({})
set([1,2,3,4])
set([1,3,3,5,5,8])
for i in set([1,3,3,4,4,5]):
    print(i)
# add an element and update a list of elements
p.add(2)
p.add("None")
p.add(None)
p
p.update([0,-3])
p

# remove elements
p.remove(0)
p.discard(100) # no error even not exist
p

# copy
p1 = p.copy()
p2 = set(p)
p1 == p2
p1 is p2
id(p1)
id(p2)

# algebra
autograd = {'autograd', 'pytorch', 'keras', 'tf', 'mxnet'}
prepare = {'pytorch','keras', 'tf', 'mxnet'}
scratch = {'autograd', 'plt', 'numpy', 'scipy'}
dl = {"pytorch", "tf", "mxnet"}
autograd.union(scratch)
autograd.intersection(scratch)
autograd.difference(prepare)
scratch.difference(autograd)
scratch.symmetric_difference(autograd)
prepare.issubset(autograd)
prepare.issubset(dl)
autograd.issuperset(prepare)
prepare.isdisjoint(dl)
prepare.isdisjoint(set("python"))
