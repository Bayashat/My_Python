"""              < 7 > List Comprehension / 列表生成式

# Syntax:
     new_ist = [expression for item in iterable if condition == True]
"""
      ## 1) don't use:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
new_list = []
                                                  
for x in fruits:                                        
  if "a" in x:                                         
    new_list.append(x)
        
print(new_list)

      ## 2) Uses:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if "a" in x]

print(new_list)  # ['apple', 'banana', 'mango']
# --------------------------------------------------------------------------------------------------------------
#                   1. Condition
# The condition is like a filter that only accepts the items that valuate to True.
# With no if statement:

new_list = [x for x in fruits]
# --------------------------------------------------------------------------------------------------------
#                   2.Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.

# Example：
new_list = [x for x in range(10)]

# Same example, but with a condition:
new_list = [x for x in range(10) if x < 5]

# Also can:
new_list = [x*x for x in range(10)]
# ----------------------------------------------------------------------------------------------------------------
#                   3.Expression
# 1.Set the values in the new list to upper case:
new_list = [x.upper() for x in fruits]

# 2.Set all values in the new list to 'hello':
new_list = ['hello' for x in fruits]

# 3.Return "orange" instead of "banana":

new_list = [x if x != "banana" else "orange" for x in fruits]
# -----------------------------------------------------------------------------------------------------------------
#                (4) Simple List 推导式
#需要将 0-10 数放入列表
    # 1. Use while loop:
list1 = []
i=0
while i<11:
    list1.append(i)
    i+=1
print(list1)    # [0,1,2,3,4,5,6,7,8,9,10]

    # 2. Use for loop:
list1 = []
for i in range(10):
    list1.append(i)
print(list1)     # [0,1,2,3,4,5,6,7,8,9,10]

    # 3.Use List 推导式:
list1 = [i for i in range(10)]
print(list1)
# --------------------------------------------------------------------------------------------------------------------
#               (5) Conditional List 推导式
# need a list with even numbers between 0-10

# Method-1: Range steps:
list1 = [i for i in range(0, 10, 2)]
print(list1)

# Method-2: Use If:
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

# --------------------------------------------------------------------------------------------------------------
#               (6) Multiple FOR List 推导式:
# Need create such List:
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

list1 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list1)

