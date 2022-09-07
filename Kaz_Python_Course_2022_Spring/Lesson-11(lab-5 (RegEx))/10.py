'''
camel case string : IGotInternAtGeeksforgeeks
snake case string : i_got_intern_at_geeksforgeeks
'''
import  re

str = input() # _I_GotInternAtGeeksforgeeks

str = re.sub(r"([a-z]*)([A-Z])", r'\1_\2', str)

if str[0] == '_':
    str = str.replace(str[0], "", 1)

str = str.lower()
print(str)