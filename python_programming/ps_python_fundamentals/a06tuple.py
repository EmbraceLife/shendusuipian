t = ('hello', 3, 4.13)
t[2]
len(t)
for i in t:
    print(i)
t + (12, 32)
t * 3
t + ((244,233))
t1 = ((1,2,3), (2,3,4))
t1
t1[0][2]
t1 = (291,)
type(t1)
t2 = (2)
type(t2)
t3 = ()
type(t3)

def return_tuple(nums):
    return max(nums), min(nums)
return_tuple([12,34,11,55])

a = "a"
b = "b"
a, b = b, a
a
b

tuple("hello")
5 in [1,2,3,4,5]
6 not in [1,2,3,4,5]
5 in (1,2,3,4,5)
6 not in (1,2,3,4,5)
