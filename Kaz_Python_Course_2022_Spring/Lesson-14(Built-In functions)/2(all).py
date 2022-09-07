# all(iterable)


'''
all()	Returns True if all items in an iterable object are true, otherwise return false

if the iterable object is empty, also return true

'''

my_list = [True, True, True]
print(all(my_list)) # True

# Note : when used on a dict, the all function checks if all keys are ture
mydict = {
    0 : "apple",
    1 : "Orange"
}

print(all(mydict)) # False