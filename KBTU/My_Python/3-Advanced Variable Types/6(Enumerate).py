#                           5. Enumerate

# Enumerate() 函数用于将一个可遍历的数据对象(如列表，元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中
# enumerate(可遍历对象, start=0)    start参数⽤来设置遍历数据的下标的起始值，默认为0。

#   1.其实我们可以这样输出 数据和下标:
my_list = ['a', 'b', 'c', 'd', 'e']

for i in my_list:
    print(my_list.index(i), i)  # 下标, 数据值

# 输出结果是: 
''' 
0 a
1 b
2 c
3 d
4 e
'''
 
# 2. 使用 Enumerate() 函数 ： 将可迭代序列中元素所在的下标和具体元素数据组合在一块，变成元组
for j in enumerate(my_list):
    print(j)

'''
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
'''

for j in enumerate(my_list, start=1):
    print(j)
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
(5, 'e')