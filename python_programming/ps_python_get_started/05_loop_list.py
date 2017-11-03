############################################
# 用for loop直接在list element 上循环
lst = ['py2', 'py3', 'web app']
for l in lst:
	print(l)

# loop on index
for i in range(len(lst)):
	if i > 0:
		print(lst[i])

# for loop 与 range的用法
r = range(3,10)
r[:]
r[0]
r[-1]

for i in range(3,10):
	print(i)

for i in range(10,3,-1):
	print(i)
