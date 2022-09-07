"""
                    < 10 > Join Lists
"""

#               1.Join Two Lists
# using the + operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)  # ['a', 'b', 'c', 1, 2, 3]
# --------------------------------------------------------------------------------------------------------------------
#           2.Another way to join two lists are by appending all the items from list2 into list1, one by one:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)  # ['a', 'b', 'c', 1, 2, 3]
# --------------------------------------------------------------------------------------------------------------------
#       3.Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)  # ['a', 'b', 'c', 1, 2, 3]
# --------------------------------------------------------------------------------------------------------------------
