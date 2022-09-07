############  58.sorted()

'''
The sorted() function returns a sorted list of the specified iterable object.
You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

Note: You cannot sort a list that contains BOTH string values AND numeric values.

# Syntax: 
sorted(iterable, key=key, reverse=reverse)

iterable	----    Required. The sequence to sort, list, dictionary, tuple etc.
key	        ----    Optional. A Function to execute to decide the order. Default is None
reverse	    ----    Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

'''

# Ex-1: Sort a tuple:

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)        # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


# Ex-2: Sort numeric:

a = (1, 11, 2)
x = sorted(a)
print(x)        # [1,2,11]


# Ex-3: Sort ascending:

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a)
print(x)        # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']



# Ex-4: Sort descending:

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)        # ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

# Ex-4: sort dict:

a = [
  {'id': 1, 'name': 'Stundet 1', 'age': 20},
  {'id': 3, 'name': 'Stundet 3', 'age': 18},
  {'id': 5, 'name': 'Stundet 5', 'age': 22},
  {'id': 4, 'name': 'Stundet 4', 'age': 21},
]

def kk(obj):
  return obj['age']

# sorted_a = sorted(a, key=kk, reverse=True)

sorted_a = sorted(a, key=lambda x: x['age'], reverse=True)
for i in sorted_a:
  print(i)

