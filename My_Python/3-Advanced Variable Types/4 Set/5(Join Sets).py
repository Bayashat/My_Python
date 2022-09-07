"""
                        < 5 > Join Two Sets
You can use the union() method that returns a new set containing all items from both sets, or the update()
    method that inserts all the items from one set into another:
"""
# -------------------------------------------------------------------------------------------------------------------
#                   (1) s1.Union(s2) or "s1|s2"
# Union 和 | 等价 : 并集操作
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)     # set3 = s1 | s2
print(set3)  # {"a", "b", "c", 1, 2, 3}
# ---------------------------------------------------------------------------------------------------------------
#                   (2) s1.Update(s2)
# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) # {"a", "b", "c", 1, 2, 3}
# -----------------------------------------------------------------------------------------------------
######   Note: Both union() and update() will exclude any duplicate items. 会排除
# -------------------------------------------------------------------------------------------------
#                   (3) s1.intersection or "s1&s2"
                ## Keep ONLY the Duplicates-1
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# intersection() 与 & 等价 : 交集操作

s1 = {"apple", "banana", "cherry"}
s2 = {"google", "microsoft", "apple"}

z = s1.intersection(s2)   # z = s1 & s2

print(z)    # "apple"

# -----------------------------------------------------------------------------------------------------------
#                   (4) s1.intersection_update(s2) :
                ##  Keep ONLY the Duplicates-2
# The intersection_update() method will keep only the items that are present in both sets.

s1 = {"apple", "banana", "cherry"}
s2 = {"google", "microsoft", "apple"}

s1.intersection_update(s2)

print(s1)    # "apple"
# ------------------------------------------------------------------------------------------------------------------
#                   (5) s1.difference(s2) or "s1-s2" :
# Find the difference of s1 in s2
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.difference(s2))    # or s1-s2 : 10

# ----------------------------------------------------------------------------------------------------------------
#                   (6) s1.symmetric_difference(s2) or "s1^s2"
#  * Keep All, But NOT the Duplicates-1
# * The symmetric_difference() method will return a new set, that contains only the elements that are NOT present
#       in both sets.

s1 = {"apple", "banana", "cherry"}
s2 = {"google", "microsoft", "apple"}

z = s1.symmetric_difference(s2) # s1^s2

print(z)    # {'google', 'banana', 'microsoft', 'cherry'}

# ---------------------------------------------------------------------------------------------------------------------
#                   (7)symmetric_difference_update():
# Keep All, But NOT the Duplicates-2
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)    # {'microsoft', 'banana', 'cherry', 'google'}
# --------------------------------------------------------------------------------------------------------------------
