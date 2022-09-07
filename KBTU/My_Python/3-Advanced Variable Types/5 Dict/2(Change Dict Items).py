"""
                < 2 > Change Dict Items
"""
#                   1.Change Values
# You can change the value of a specific item by referring to its key name:
# dict[key] = value  # 如果key存在，会修改成value, 若key不存在，则会添加这个key和value.

this_dict = {"brand": "Ford",
             "model": "Mustang",
             "year": 2018,
             'name': 'issac'}
# -----------------------------------------------------------------------------------------------------------
#                   2.Update Dictionary : 合并另一个字典
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.update({"year": 2020})
# ----------------------------------------------------------------------------------------------------------------
# 注意 : 在dict, int 的1 和 float 的1.0 代表一个key值

