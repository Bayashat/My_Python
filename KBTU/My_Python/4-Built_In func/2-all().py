############  2.all()
# Syntax:
all(iterable)

'''

The all() function returns True if all items in an iterable are true, otherwise it returns False.

If the iterable object is empty, the all() function also returns True

'''
##  Ex-1:

mylist = [True, True, True]
x = all(mylist)     # True

'''
*********************************************************************************************************************
'''
## Ex-2:

# Check if all keys in a dictionary are True:

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)  # False

# Note: When used on a dictionary, the all() function checks if all the keys are true, not the values.

'''
*********************************************************************************************************************
'''

def my_all(iterable):
  for item in iterable:
    if not item:
      return False
  return True


print(my_all([True, True, True]))
print(my_all([True, False, True]))

print(my_all((1, 0, 'hello')))
print(my_all('hello'))
print(my_all(''))

