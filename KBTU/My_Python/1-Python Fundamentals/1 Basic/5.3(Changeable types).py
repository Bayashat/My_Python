# 在python中，值是靠引用来传递来的。
# 我们可以⽤id()来判断两个变量是否为同一个值的引用. 我们可以将id值理解为那块内存的地址标识。

# 所谓可变类型与不可变类型是指: 数据能够直接进行修改, 如果能直接修改那么就是可变, 否则是不可变

#                       1.Unchangeable type/不可变类型: int, float, string, tuple
a = 10
b = a

print(b)  # 10

print(id(a))    # 2697645484336
print(id(b))    # 2697645484336

a = 20

print(b)    # 10

print(id(a))    # 2697645484368
print(id(b))    # 2697645484336  没有随a而变,is unchangeable

#                       2. Changeable types/可变类型: List, Dict, Set
a = [10, 20]
b = a

print(b)  # [10,20]

print(id(a))    # 1563466679872
print(id(b))    # 1563466679872

a.append(30)

print(b)        # [10,20,30]  是可变类型, so 随着 a 变了

print(id(a))    # 1563466679872
print(id(b))    # 1563466679872


