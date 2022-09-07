############   19.eval()

'''
The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.

# Syntax; 
eval(expression, globals, locals)

expression	----    A String, that will be evaluated as Python code

globals	    ----    Optional. A dictionary containing global parameters

locals	    ----    Optional. A dictionary containing local parameters

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Evaluate the expression 'print(55)':

x = 'print(55)'
eval(x)
