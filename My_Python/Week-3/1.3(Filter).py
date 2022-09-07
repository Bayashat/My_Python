#                       1.3 Filter / 过滤函数
# filter(func, lst) 函数用于过滤序列, 过滤掉不符合条件的元素, 返回一个 filter 对象. 如果要转换为列表,可以使⽤ list() 来转换

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x % 2 == 0


result = filter(func, list1)
# or
result = filter(lambda x: x % 2 == 0, list1)

print(result)  # <filter object at 0x0000017AF9DC3198>
print(list(result))  # [2, 4, 6, 8, 10]
