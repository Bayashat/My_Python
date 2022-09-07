################  48-pow()

'''
The pow() function returns the value of x to the power of y (xy).
If a third parameter is present, it returns x to the power of y, modulus z.

# Syntax : 
pow(x, y, z)

x	A number, the base
y	A number, the exponent
z	Optional. A number, the modulus

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)   # 64

# Ex-2: Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):

x = pow(4, 3, 5)    # 4