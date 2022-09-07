#########  52-range()

'''
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# Syntax : 
range(start, stop, step)

start	----    Optional. An integer number specifying at which position to start. Default is 0
stop	----    Required. An integer number specifying at which position to stop (not included).
step	----    Optional. An integer number specifying the incrementation. Default is 1

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Create a sequence of numbers from 0 to 5, and print each item in the sequence:

x = range(6)
for n in x:
  print(n)  # 0 1 2 3 4 5



# Ex-2: Create a sequence of numbers from 3 to 5, and print each item in the sequence:

x = range(3, 6)
for n in x:
  print(n)  # 3 4 5


# Ex-3:  Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:

x = range(3, 20, 2)
for n in x:
  print(n)  # 3 5 7 9 11 13 15 17 19
  

