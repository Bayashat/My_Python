#########  3.any()

# Syntax:
any(iterable)

#iterable  ------- An iterable object (list, tuple, dictionary)

'''
The any() function returns True if any item in an iterable are true, otherwise it returns False.

If the iterable object is empty, the any() function will return False.
'''

## Ex-1:  Check if any item in a set is True:

myset = {0, 1, 0}
x = any(myset)      # True

'''
*************************************************************************************************************
'''
## Ex-2: Check if any item in a dictionary is True:

mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)     # True

# Note: When used on a dictionary, the any() function checks if any of the keys are true, not the values.

'''
*************************************************************************************************************
'''

def my_any(iterable):
  for item in iterable:
    if item:
      return True
  return False


print(my_any([True, False, False]))
print(my_any([0, False, False]))
print(my_any([0, 0, 0]))