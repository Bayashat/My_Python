        #       < 2.1> 输⼊
# 在Python中，程序接收用户输入的数据的功能即是输⼊： 从键盘获取输入的内容，存入计算机程序中

--------------------------------------------------------------------------------------------------------------

#   < 2.2 > 
#  Python 3.6 uses the input() method.

# Python 2.7 uses the raw_input() method.

# Python 3.6
username = input("Enter username:")
print("Username is: " + username)

# Python 2.7
username = raw_input("Enter username:")
print("Username is: " + username)
--------------------------------------------------------------------------------------------------------------

#  < 2.3 > 输⼊的特点
1.遇到input,等待用户输入
2.  input 接收⽤户输入后，⼀般存储到变量，⽅便使用。
3. input 接受到的数据类型都是 str

password = input('请输入您的密码：')
print(f'您输入的密码是{password}')

print(type(password))   # <class 'str'>

-------------------------------------------------------------------------------------------------------------------