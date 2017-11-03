import a02_lib
a02_lib.__doc__
a02_lib.__file__
a02_lib.__name__
dir(a02_lib)
a02_lib.a02.__file__
dir(a02_lib.a02)

# check classes can be directly assessed
dir(a02_lib)
a = a02_lib.a02.A02()
a = a02_lib.A02()
a.purpose()



############################
# to bring A02 one step closer to outer side of package
# __init__.py
# insert: from a02_lib.a02 import A02
