"""
                  < 4 > Remove Dict Items
"""

#                   (1) Dict.pop(key) : 按key值删除，返回值是删除的key对应的value.
# The pop() method removes the item with the specified key name:

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
result = this_dict.pop("model")  # 可以将删除的value接受
print(result)  # "Mustang"

# ------------------------------------------------------------------------------------------------------------------
#                 (2) Dict.popitem()
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.popitem()
print(this_dict)  # {'brand': 'Ford', 'model': 'Mustang'}

# -----------------------------------------------------------------------------------------------------------------
#                 (3) del dict[key]  根据key值删除数据
# The del keyword removes the item with the specified key name:

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del this_dict["model"]   # 删除指定的键值对
print(this_dict)
# ---------------------------------------------------------------------------------------------------------
#               (4) del Dict : 直接将这个字典删除了. 后面的代码不能再直接使用这个变量了，除法再次定义.
# The del keyword can also delete the dictionary completely:

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del this_dict  # or:  del(this_dict)
print(this_dict)  # Error
# ------------------------------------------------------------------------------------------------------------------
#               (5) The clear() method empties the dictionary: 清空,删除所有的键值对

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.clear()
print(this_dict)  # {}


