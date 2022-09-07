#########   4.Ascii.()

# Syntax : 

ascii(object)

# object	    An object, like String, List, Tuple, Dictionary etc.

'''
The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).

The ascii() function will replace any non-ascii characters with escape characters:

å will be replaced with \xe5

'''


'''
*********************************************************************************************************************
'''


## Ex-1 : Escape non-ascii characters:

x = ascii("My name is Ståle")   #  'My name is St\e5le' 