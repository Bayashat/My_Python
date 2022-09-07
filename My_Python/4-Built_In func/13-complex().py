############    13.compledx()

'''
The complex() function returns a complex number by specifying a real number and an imaginary number.
'''

# Syntax
complex(real, imaginary)

'''
real	----  Required. A number representing the real part of the complex number. Default 0. 
                  The real number can also be a String, like this '3+5j', when this is the case, the second parameter should be omitted

imaginary	----  Optional. A number representing the imaginary part of the complex number. Default 0.

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Convert the number 3 and imaginary number 5 into a complex number:

x = complex(3, 5)   # (3+5j)

# Ex-2: Convert a string into a complex number:

x = complex('3+5j') # (3+5j)
