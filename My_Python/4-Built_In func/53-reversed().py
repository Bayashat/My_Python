###############   53.reversed()

'''

The reversed() function returns a reversed iterator object.

# Syntax:
reversed(sequence)

sequence	----    Required. Any iterable object

'''

'''
*********************************************************************************************************************
'''


# Ex-1: Reverse the sequence of a list, and print each item:

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)  # d c b a 