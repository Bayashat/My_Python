'''
需求：⽤用户输⼊入当前⽬目录下任意⽂文件名，程序完成对该⽂文件的备份功能(备份⽂文件名为xx[备份]后缀，例例
如：test[备份].txt)

# 1. 接收用户输⼊⽬标文件名
# 2 规划备份文件的名字
# 3.备份文件写入数据(数据和原文件一样)
# 4. 思考: 有效文件才备份: .txt

'''
# 1. 接收用户输⼊⽬标文件名
old_name = input('请输⼊您要备份的文件名：')

# 2 规划备份文件的名字
# 2.1 提取后缀--找到名字中的点--名字和后缀分离 --最右侧的点才是后缀的点
index = old_name.rfind('.')

# 4. 思考: 有效文件才备份: .txt
if index > 0:
    # 提取后缀
    postfix = old_name[index:]
    
# 2.2 组织新名字 = 原名字 + [备份] + 后缀
# 原名字就是字符串中的一部分字串 -- 切片[start, end, step]
# print(old_name[:index])  -- 原名字
# print(old_name[index:])  -- 后缀

# new_name = old_name[:index] + '[备份]' + old_name[index:]
new_name = old_name[:index] + '[备份]' + postfix

# 3.备份文件写入数据(数据和原文件一样)
# 3.1 打开 原文件 和 备份文件
old_f = open(old_name, 'rb')
new_f =open(new_name, 'wb')

# 3.2 原文件读取, 备份文件写入
# 如果不确定目标文件大小,循环读取写入,当读取出来的数据没有了,终止循环
while True:
    con  = old_f.read(1024)
    if (len(con)) == 0:
        # 表示读取完成了
        break
    new_f.write(con)

# 3.3 关闭文件
old_f.close()
new_f.close()