"""
                    < 10 > Dict comprehension
"""

#               (1) 创建一个字典：字典key是1-5数字，value是这个数字的2次⽅
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16}


#               (2.1) 将两个列表合并为一个字典:
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)
#  If the length isn't same , take the shortest length.

#               (2.2) 将两个列表合并为一个字典,使用 zip()函数:
# 内置函数Zip(): 用于将可迭代的对象作为参数,将对象中对应的元素打包成一个元组,然后返回由这些元组组成的列表
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
"""
l = zip(items, prices)
print(list(l))      # [('Fruits', 96), ('Books', 78), ('Others', 85)]
print(dict(l))      # {'Fruits': 96, 'Books': 78, 'Others': 85}
"""
d = {item: price for item, price in zip(items, prices)}
print(d)    # {'Fruits': 96, 'Books': 78, 'Others': 85}

#               (2.3) 提取字典中目标数据:
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求：提取上述电脑数量大于等于200的字典数据

count1 = {key: value for key, value in counts.items() if value >= 200}

print(count1)  # {'MBP': 268, 'DELL': 201}

