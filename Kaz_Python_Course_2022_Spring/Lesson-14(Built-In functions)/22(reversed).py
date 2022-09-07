'''
reversed()	Returns a reversed iterator
'''

s = "hello"
s2 = reversed(s)
for i in s2:
    print(i, end = '')

l = ["a", "b", "c", "d"]
l2 = reversed(l)
for i in l2:
    print(i)
