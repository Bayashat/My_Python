"""
                    < 6 > Iterate Dict
"""

this_dict = {'name': 'issac',
             'age': 18,
             'gender': 'male'
             }

#                   1.循环直接遍历字典, 遍历的是key.  Print all key names in the dictionary, one by one: for

for x in this_dict:
    print(x)  # 'name', 'age', 'gender'

# --------------------------------------------------------------------------------------------------------------------
#                   2.Print all values in the dictionary, one by one: 这样遍历 value 值

for x in this_dict:
    print(this_dict[x])  # 'issac', 18, 'male'

# -------------------------------------------------------------------------------------------------------------------
#                   3. 直接遍历key和value值:

for x in this_dict:
    print(x, this_dict[x])

# --------------------------------------------------------------------------------------------------------------------
#                   4.dict.values()
# 获取所有的value值，类型是 dict_values
# 1. 可以使用list() 进行类型转换，即将其转换为列表类型
# 2. 可以使用for循环进行遍历

for x in this_dict.values():
    print(x)  # 'issac' 18 'male'

# -----------------------------------------------------------------------------------------------------------------
#                   5.dict.keys()
# 获取字典中所有的key值，得到的类型是dict_keys, 该类型具有的特点是:
# 1. 可以使用list() 进行类型转换，即将其转换为列表类型
# 2. 可以使用for循环进行遍历

for x in this_dict.keys():
    print(x)  # name age gender

# -----------------------------------------------------------------------------------------------------------------
#                   6.dict.items()
#  获取所有的键值对，类型是dict_items
# 1. 可以使用list() 进行类型转换，即将其转换为列表类型
# 2. 可以使用for循环进行遍历

for x, y in this_dict.items():
    print(x, y)  # { name: issac, age:18, gender:male }

for item in this_dict.items():
    print(item[0], item[1])

for key, value in this_dict.items():
    print(f'{key}={value}')
# -----------------------------------------------------------------------------------------------------------------
