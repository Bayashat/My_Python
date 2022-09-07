####################   41.min()

'''
The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.

If the values are strings, an alphabetically comparison is done.

# Syntax: 
min(n1, n2, n3, ...)
# Or:
min(iterable)

n1, n2, n3, ...	One or more items to compare

iterable	An iterable, with one or more items to compare

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Return the lowest number:

x = min(5, 10)  # 5

# Ex-2: Return the name with the lowest value, ordered alphabetically:

x = min("Mike", "John", "Vicky")    # John

# Ex-3: Return the item in a tuple with the lowest value:

a = (1, 5, 3, 9)
x = min(a)      # 1

