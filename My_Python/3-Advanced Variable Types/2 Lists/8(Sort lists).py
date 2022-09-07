"""
                      < 8 > Sort Lists
"""

#                   1.Sort List Alphanumerically

this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)  # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# --------------------------------------------------------------------------------------------------------------------
#                   2.Sort the list numerically:

this_list = [100, 50, 65, 82, 23]
this_list.sort()
print(this_list)  # [23, 50, 65, 82, 100]

# --------------------------------------------------------------------------------------------------------------------
#                   3.Sort Descending : 若想从大到小排序，使用: list.sort(reverse=True)
# 语法 ： 列表序列.sort(key=None, reverse=false)
# reverse = True 是降序 , reverse = False 是升序

this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort(reverse=True)
print(this_list)  # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

this_list = [100, 50, 65, 82, 23]
this_list.sort(reverse=True)
print(this_list)  # [100, 82, 65, 50, 23]

# --------------------------------------------------------------------------------------------------------------------
#                   4 sorted(list) : 不会在原列表中进行排序, 会得到一个新的列表:
my_list = [3, 7, 4, 2, 8, 5, 3]
my_list2 = sorted(my_list)
print(my_list2)  # [2,3,3,4,5,7,8]

my_list2 = sorted(my_list, reverse=True)
print(my_list2)  # [[8, 7, 5, 4, 3, 3, 2]]


# --------------------------------------------------------------------------------------------------------------------
#                   5.Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# Sort the list based on how close the number is to 50:

def myfunc(n):
    return abs(n - 50)


this_list = [100, 50, 65, 82, 23]
this_list.sort(key=myfunc)
print(this_list)  # [50, 65, 23, 82, 100]
# --------------------------------------------------------------------------------------------------------------------
#                   6.Case Insensitive Sort
# 若不区分大小写会先将大的sort:

this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort()
print(this_list)  # ['Kiwi', 'Orange', 'banana', 'cherry']

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:

this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort(key=str.lower)
print(this_list)  # ['banana', 'cherry', 'Kiwi', 'Orange']
# --------------------------------------------------------------------------------------------------------------------
#                   7.Reverse Order : 会改变原列表

this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.reverse()
print(this_list)  # ['cherry', 'Kiwi', 'Orange', 'banana']
# --------------------------------------------------------------------------------------------------------------------
#                   8.逆置.[::-1] : get a new list
this_list = [1, 2, 3, 4, 5]
xx = this_list[::-1]
print(xx)  # 5,4,3,2,1
