'''
需求：把code 文件夹所有文件重命名 python xxx
步骤:

1. 找到所有文件: 获取 code 文件夹的目录列表 -- listdir()
2. 构造名字
3.重命名

'''
import os

# 1. 找到所有文件: 获取 code 文件夹的目录列表 -- listdir()
file_list = os.listdir()
print(file_list)


# 2. 构造名字
for i in file_list:
    # new_name = 'Python_' + 原文件i
    new_name = 'Python_' + i

# 3.重命名
    os.rename(i, new_name)