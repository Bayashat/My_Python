##########   17.divmod()

'''

The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).

# Syntax
divmod(dividend, divisor)

dividend	---     A Number. The number you want to divide

divisor	    ---     A Number. The number you want to divide with
'''

def my_divmod(a, b):
  return (int(a / b), a % b)

'''
*********************************************************************************************************************
'''

# Ex-1: Display the quotient and the remainder of 5 divided by 2:

x = divmod(5, 2)    # (2,1)

