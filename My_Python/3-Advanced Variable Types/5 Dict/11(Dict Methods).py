"""
                        < 9 > Dict Methods

Python has a set of built-in methods that you can use on dictionaries.

clear()-----------------Removes all the elements from the dictionary
copy()------------------Returns a copy of the dictionary
fromkeys()-------------Returns a dictionary with the specified keys and value
get()-----------------Returns the value of the specified key
items()---------------Returns a list containing a tuple for each key value pair
keys()----------------Returns a list containing the dictionary's keys
pop()----------------Removes the element with the specified key
popitem()------------Removes the last inserted key-value pair
setdefault()---------Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()-------------Updates the dictionary with the specified key-value pairs
values()---------------Returns a list of all the values in the dictionary

#  Python字典包含了以下内置函数：

1.	len(dict)       计算字典元素个数，即键的总数。
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> len(dict)
3

2.	str(dict)        输出字典，以可打印的字符串表示。
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> str(dict)
"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"

3.	type(variable)  返回输入的变量类型，如果变量是字典就返回字典类型。
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> type(dict)
<class 'dict'>

#  Python字典包含了以下内置方法：

1	radiansdict.clear()         删除字典内所有元素
2	radiansdict.copy()          返回一个字典的浅复制
3	radiansdict.fromkeys()      创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)      返回指定键的值，如果键不在字典中返回 default 设置的默认值
5	key in dict                 如果键在字典dict里返回true，否则返回false
6	radiansdict.items()         以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()          返回一个迭代器，可以使用 list() 来转换为列表
8	radiansdict.setdefault(key, default=None)       和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)    把字典dict2的键/值对更新到dict里
10	radiansdict.values()         返回一个迭代器，可以使用 list() 来转换为列表
11	pop(key[,default])           删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12  popitem()                   随机返回并删除字典中的最后一对键和值。
"""