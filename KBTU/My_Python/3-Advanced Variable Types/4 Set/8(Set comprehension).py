"""
                < 8 > Set Comprehension - Set 生成式
"""
# Need: Create a set with square of this list:
list1 = [1, 1, 2]

# Solution:
set1 = {i ** 2 for i in list1}  # or [i*i for i in list1]

print(set1)  # {1, 4}
# 集合有去重功能

