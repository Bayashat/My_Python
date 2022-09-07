"""
                    < 5 > Join Tuples
"""
#                   1.Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)     # ('a', 'b', 'c', 1, 2, 3)
# ------------------------------------------------------------------------------------------------------------------
#                   2.Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2

print(my_tuple)  # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

