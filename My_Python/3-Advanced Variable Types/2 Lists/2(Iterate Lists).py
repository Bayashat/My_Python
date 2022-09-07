"""
                  < 2 > Iterate Lists

"""

#                 1.Loop Through a List
this_list = ["apple", "banana", "cherry"]
for x in this_list:
  print(x)
# --------------------------------------------------------------------------------------------------------------------
#                 2.Loop Through the Index Numbers
this_list = ["apple", "banana", "cherry"]
for i in range(len(this_list)):
  print(this_list[i])
# -----------------------------------------------------------------------------------------------------------------
#                 3.sing a While Loop
this_list = ["apple", "banana", "cherry"]
i = 0
while i < len(this_list):
  print(this_list[i])
  i+=  1
# -----------------------------------------------------------------------------------------------------------------
              ##   4.Looping Using List Comprehension
# A short hand for loop that will print all items in a list:

this_list = ["apple", "banana", "cherry"]
[print(x) for x in this_list]   # ["apple", "banana", "cherry"]

# ----------------------------------------------------------------------------------------------------------------
