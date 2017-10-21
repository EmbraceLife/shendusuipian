# 如何使用break, continue
lst = ["py2", "py3", "numpy", "scipy"]

for l in lst:
	if l.startswith("py"):
		print("got pre_py!")
	elif l.endswith("py"):
		print("got sufix_py!")
	if l.find("n"):
		print("n is not found")
	elif not l.find("n"):
		print("n is found in %s" % l)
	print(l, "is looped -----")
for l in lst:
	if l.startswith("py"):
		continue
		print("got pre_py!")
	elif l.endswith("py"):
		print("got sufix_py!")
	if l.find("n"):
		print("n is not found")
	elif not l.find("n"):
		print("n is found in %s" % l)
	print(l, "is looped -----")
for l in lst:
	if l.startswith("py"):
		break
		print("got pre_py!")
	elif l.endswith("py"):
		print("got sufix_py!")
	if l.find("n"):
		print("n is not found")
	elif not l.find("n"):
		print("n is found in %s" % l)
	print(l, "is looped -----")

for l in lst:
	for l in lst:
		if l.startswith("py"):
			break
			print("got pre_py!")
		elif l.endswith("py"):
			print("got sufix_py!")
		if l.find("n"):
			print("n is not found")
		elif not l.find("n"):
			print("n is found in %s" % l)
		print(l, "is looped -----")
	print("subloop is done")
