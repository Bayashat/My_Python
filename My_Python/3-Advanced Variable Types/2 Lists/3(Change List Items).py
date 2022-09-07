"""
                    < 3 > Change List Items

"""

#                       1.Change Item Value

this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"
print(this_list)     # ["apple", "blackcurrant", "cherry"]

# ----------------------------------------------------------------------------------------------
#                       2.Change a Range of Item Values

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# ---------------------------------------------------------------------------------------------------------

#                       3.
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items
#                        will move accordingly:

this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

# ----------------------------------------------------------------------------------------------------------------
#                       4.
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)  # ['apple', 'watermelon']
# --------------------------------------------------------------------------------------------------------