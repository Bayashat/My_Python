##################  39.map()

'''
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# Syntax: 
map(function, iterables)

function	----    Required. The function to execute for each item
iterabl     ----    Required. A sequence, collection or an iterator object. You can send as many iterables as you like, 
                        just make sure the function has one parameter for each iterable.    

'''
def myfunc(n):
  return len(n)

def my_map(func, iterable):
  for item in iterable:
    yield func(item)
  

x = my_map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))


'''
*********************************************************************************************************************
'''


# Ex-1: Calculate the length of each word in the tuple:
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x) 
     # <map object at 0x056D44F0>

#convert the map into a list, for readability:
print(list(x))  # [5, 6, 6]

# Ex-2: Make new fruits by sending two iterable objects into the function:

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)        # <map object at 0x034244F0>

#convert the map into a list, for readability:
print(list(x))  # ['appleorange', 'bananalemon', 'cherrypineapple']

