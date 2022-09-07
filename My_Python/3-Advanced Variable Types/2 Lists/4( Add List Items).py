"""                 < 4 > Add list Items
向列表中添加数据的方法，都是直接在原列表中进行添加的，不会返回新的列表.
* 可变
"""

a = list(input().split())

#                   (1) list.append( "Value" ) : 向列表尾部追加数据
# 如果追加的数据是一个序列，则追加整个序列到列表

this_list = ["apple", "banana", "cherry", "orange"]
print(this_list) # ["apple", "banana", "cherry"， "orange"]

this_list.append([11,22])
print(this_list) # ["apple", "banana", "cherry"， "orange",[11,22] ]

# ---------------------------------------------------------------------------------------------------------------
#                   (2) list.insert("Index", "Value" ) :  在指定的下标位置前进行添加数据
# The insert() method inserts an item at the specified index:

my_list = ["apple", "banana", "cherry"]
my_list.insert(2, "orange")

print(my_list)  # ["apple", "banana","orange", "cherry"]

# ---------------------------------------------------------------------------------------------------------------
#                   (3) list.Extend("Iterate Object")  str and list : 会将可迭代对象中的数据逐个添加到原列表的末尾.
# 若追加数据是list,会逐一添加

# Add the elements of "tropical" to "thislist":

this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

my_list = [1,'issac',2]
my_list.extend('hel')
print(my_list)  # [1, 'issac', 2, 'h', 'e', 'l']  # 会将序列(可迭代对象)拆开加入

# ---------------------------------------------------------------------------------------------------------------------
#                   (4) Use +=
my_list = ["banana", "Orange", "Kiwi", "cherry"]
x = [1, 2, 3]

my_list += x

print(my_list) # ['banana', 'Orange', 'Kiwi', 'cherry', 1, 2, 3]

# -------------------------------------------------------------------------------------------------------------------
#                   (5) Add Any Iterable
# Add elements of a tuple to a list:

this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
# ------------------------------------------------------------------------------------------------------------------
