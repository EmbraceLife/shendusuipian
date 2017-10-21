pydict = {
	"name": "py3",
	"list": [2,3,4],
	"none": None}

pydict

pydicts = [pydict, {'py2': "outdated"}]

pydict.keys()

pydict.values()

pydict['name'] = "py3.6"

del pydict["none"]

pydict
# del pydict[-1]

for k, v in pydict.items():
	print(k, v)

pydict.
