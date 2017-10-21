pydict = {"name": "py3","list": [2,3,4],"none": None}
pydict
# pydict['func']
# num = 3 + pydict['name']

try:
    func = pydict['func']
except KeyError:
    print("pydict['func'] is not given yet")


try:
    num = 3 + pydict['name']
except TypeError:
    print("num+str is the problem")


try:
    num = 3 + pydict['name']
except Exception as e:
    print("num+str is the problem")
    print(e)


pydict['attr'] = 100
pydict
