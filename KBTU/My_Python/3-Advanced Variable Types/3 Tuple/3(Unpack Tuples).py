"""
                        < 3 > Unpack Tuples
"""
#                   1.Packing a tuple:

fruits = ("apple", "banana", "cherry")
# ------------------------------------------------------------------------------------------------------
#                   2.in Python, we are also allowed to extract the values back into variables.
#                   This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)   #apple
print(yellow)  #banana
print(red)     #cherry
# ------------------------------------------------------------------------------------------------------------------
"""
Note: The number of variables must match the number of values in the tuple, if not,
                you must use an asterix to collect the remaining values as a list.
"""
# ------------------------------------------------------------------------------------------------------------------
#                   3.Using Asterix*-1
# If the number of variables is less than the number of values, you can add an * to the variable name and the values
#                 will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)    # apple
print(yellow)   # banana
print(red)      # ['cherry', 'strawberry', 'raspberry']
# -----------------------------------------------------------------------------------------------------------------
#                   4.Using Asterix*-2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)    # apple
print(tropic)   # ['mango', 'papaya', 'pineapple']
print(red)      # cherry

