'''
any(iterable)	Returns True if any item in an iterable object is true, otherwise return false

if the iterable object is empty, also return false
'''

myset = {0,1,0}
print(any(myset))  # true

# Note : when used on a dict, the all function checks if all keys are ture
mydict = {
    0 : "apple",
    1 : "Orange"
}

print(any(mydict)) # True
