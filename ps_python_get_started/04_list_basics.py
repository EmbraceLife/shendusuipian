############################################
lst = ['py2', 'py3', 'web app']
lst1 = lst # same address or referece, thanks to C pointer
lst2 = lst.copy()
lst.append('data science')
lst
lst1
lst2
# slice
lst[0]
lst[-1]
lst[-2]
lst.index("py2")
lst.index("data science")
lst.insert(0,"python")
lst
# is in or not
"python" in lst
"python2" in lst
# check length
lst.__len__()
len(lst)
# delete element
lst.__delitem__(-1)
lst
del lst[0]
lst
# slicing
lst[1:]
lst[1:-1]
# pop: remove and output last element
lst
lst.pop()
lst
