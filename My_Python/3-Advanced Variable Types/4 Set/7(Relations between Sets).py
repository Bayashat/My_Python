"""
                        < 7 >  集合间的关系 / Relations between sets
"""

#       <1> 两个集合是否相等: ==
""" 可以使用运算符 == 或 != 进行判断"""
set1 = {10, 20, 30, 40}
set2 = {30, 40, 20, 10}
print(set1 == set2)  # True
print(set1 != set2)  # False

#       <2> 一个集合是否是另一个集合的子集 : s1.issubset(s2)
""" 可以调用 issubset 方法进行判断"""
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))  # True
print(s3.issubset(s1))  # False


#       <3> 一个集合是否是另一个集合的超集 : s1.issuperset(s2)
"""可以调用 issuperset 方法进行判断"""

print(s1.issuperset(s2))    # True
print(s1.issuperset(s3))    # False


#       <4> 两个集合是否没有交集 : s1.isdisjoint(s2)
"""可以调用isdisjoint方法进行判断"""
print(s2.isdisjoint(s3))    # False 代表有交集

s4 = {100, 200, 300}
print(s2.isdisjoint(s4))    # True 代表没有交集

