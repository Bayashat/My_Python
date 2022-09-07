"""
                      < 1 > Access Dict items
 * 在dict访问元素, 是没有下标的概念的.
"""
#                     1.Accessing Items-1 : 使用key值访问对应的value值
# You can access the items of a dictionary by referring to its key name, inside square brackets:

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
            }
print(this_dict["model"])  # "Mustang"

print(this_dict["xaxax"]) # Error  若访问没有的key,会报错
# ----------------------------------------------------------------------------------------------------------------
#                     2. Get.()
# There is also a method called get() that will give you the same result:

print(this_dict.get("model")) # "Mustang"

print(this_dict.get("xaxax")) # "None"  用 get访问没有的key,会返回NONE

# -------------------------------------------------------------------------------------------------------------------
#                     3. Get(key,数据值)  如果key存在，返回key对应的value, 若key不存在,返回书写的数据值.若不写数据值，返回None.
                            # 但是对原dict不影响
my_dict = {'name': "issac",'age':18, "country":"KZ"}
print(my_dict.get('age',1))  # 18
print(my_dict.get('hobby',"foot")) # foot
print(my_dict)  # 'name': "issac",'age':18, "country":"KZ"

# -------------------------------------------------------------------------------------------------------------------
#                   4. Keys() : get keys  查找字典中所有的key,返回可迭代对象.
# The keys() method will return a list of all the keys in the dictionary.

print(this_dict.keys()) # dict_keys(['brand', 'model', 'year'])

# --------------------------------------------------------------------------------------------------------------------
#                   5.values() : get values  查找字典中所有的value,返回可迭代对象.
# The values() method will return a list of all the values in the dictionary.

print(this_dict.values())  # dict_values(['Ford', 'Mustang', 1964])

# ---------------------------------------------------------------------------------------------------------------------
#               6.items() : get items  查找字典中所有的键值对，返回可迭代对象.里面的数据是元组.元组数据1是字典的key.数据2是value
# The items() method will return each item in a dictionary, as tuples in a list.

print(this_dict.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# --------------------------------------------------------------------------------------------------------------------
#               7.Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in this_dict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


