#                           2. Del
# Del or del() : 删除

#               1. Str 字符串 : 不支持下标删除
str1 = 'abcdefg'
del str1
print(str1)  # Error. Have been deleted

# -------------------------------------------------------------------------------------------
#               2. List 列表
list1 = [10, 20, 30, 40]
del (list1[0])
print(list1)  # [20, 30, 40]
del list1
print(list1)  # ERROR  Have been deleted

# ---------------------------------------------------------------------------------------------
#               3. Tuple 元组: 不支持del
t1 = (10, 20, 30, 40, 50)
del t1[0]
print(t1)  # ERROR 不支持删除

# ---------------------------------------------------------------------------------------------
#               4.Set 集合 : 不支持下标删除

s1 = {10, 20, 30, 40, 50}
del s1
print(s1)  # Error, have been deleted

# ---------------------------------------------------------------------------------------------
#               5.Dict 字典 :

dict1 = {'name': 'Maks', 'age': 18}
del dict1['name']
print(dict1)  # {'age': 18}

del dict1
print(dict1)  # Error, have been deleted
