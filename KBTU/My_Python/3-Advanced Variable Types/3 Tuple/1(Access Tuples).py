"""
                    < 1 > Access Tuples
"""

#                     1.Access Tuple Items

this_tuple = ("apple", "banana", "cherry")
print(this_tuple[1])   # “banana"
# ----------------------------------------------------------------------------------------------------------------
#                     2.Negative Indexing
# -1 refers to the last item, -2 refers to the second last item etc.

this_tuple = ("apple", "banana", "cherry")
print(this_tuple[-1])    # "cherry"

# --------------------------------------------------------------------------------------------------------------------
#                     3.Range of Indexes

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[2:5])

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[:4])

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[2:])
# --------------------------------------------------------------------------------------------------------------------
#                     4.Range of Negative Indexing

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[-4:-1])
# ---------------------------------------------------------------------------------------------------------------------
#                     5.Check if Item Exists

this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
  print("Yes, 'apple' is in the fruits tuple")
# --------------------------------------------------------------------------------------------------------------------
#                     6.Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround.You can convert the tuple into a list, change the list,and convert the list back into a tuple.

# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# ----------------------------------------------------------------------------------------------------------------
#                     7.Add Items
# Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back
#             into a tuple.

this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.append("orange")
this_tuple = tuple(y)

# --------------------------------------------------------------------------------------------------------------
#                   8.Remove Items
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.remove("apple")
this_tuple = tuple(y)

# -------------------------------------------------------------------------------------------------------------
#                 9.Delete Items
# The del keyword can delete the tuple completely:

this_tuple = ("apple", "banana", "cherry")
del this_tuple
print(this_tuple) #this will raise an error because the tuple no longer exists
# ---------------------------------------------------------------------------------------------------------------
