#############  40.max()

'''

The max() function returns the item with the highest value, or the item with the highest value in an iterable.

If the values are strings, an alphabetically comparison is done.

# Syntax: 
max(n1, n2, n3, ...)
 # Or:
max(iterable)

n1, n2, n3, ...	One or more items to compare

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Return the largest number:

x = max(5, 10)  # 10


# Ex-2: Return the name with the highest value, ordered alphabetically:

x = max("Mike", "John", "Vicky")    # Vicky

# Ex-3: Return the item in a tuple with the highest value:

a = (1, 5, 3, 9)
x = max(a)      # 9