##########################          1.Open file


# The open() function returns a file object, which has a read() method for reading the content of the file:
打开文件,是文件从硬盘中存到内存中.


open(name, mode, encoding=None)

# The open() function takes two parameters; filename, and mode.

'''
name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
mode：设置打开文件的模式(访问模式)：只读、写⼊、追加等.
encoding: 文件的编码格式,常见的有gbk, utf-8 

open 的返回值是文件对象,后续所有的文件操作,都需要通过这个文件对象进行.
'''
# There are four different methods (modes) for opening a file . 访问模式可以省略,代表只读:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist. 如果文件不存在则报错。不支持写入操作，表示只读

"a" - Append - Opens a file for appending, creates the file if it does not exist  追加.若文件不存在,新建文件. 如果执行写入,在原有内容基础上,追加新内容. 指针会在文件末尾.

"w" - Write - Opens a file for writing, creates the file if it does not exist. 只写.若文件不存在,新建文件.如果执行写入,会覆盖内容.

"x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

## Syntax
# To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
# or
f = open("demofile.txt", "rt")

# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# Note: Make sure the file exists, or else you will get an error.

'''
-------------------------------------------------------------------------------------------------------------------------------------
'''
                            #### 1.Open file on the server and read it

'''
⽂件对象.read(num)

num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据。
'''
## 1).
# we have a "test.txt"
# To open the file, use the built-in open() function.

f = open("test.txt", "r")
print(f.read())

'''
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
'''

## 2).If the file is located in a different location, you will have to specify the file path, like this:

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

'''
-------------------------------------------------------------------------------------------------------------------------------------
'''
                        #### 2.Read Only Parts of the File

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# 1).
# Return the 5 first characters of the file:

f = open("test.txt", "r")
print(f.read(5))    # "Hello"

'''
-------------------------------------------------------------------------------------------------------------------------------------
'''
                        ##### 3. Read lines
# You can return one line by using the readline() method: readline()一次读取⼀行内容。

# 1).
# Read one line of the file:

f = open("test.txt", "r")
print(f.readline())     # Hello! Welcome to demofile.txt

# 2). By calling readline() two times, you can read the two first lines:
f = open("test.txt", "r")
print(f.readline())
print(f.readline())

'''
Hello! Welcome to demofile.txt
This file is for testing purposes.
'''

# 3). By looping through the lines of the file, you can read the whole file, line by line:
f = open("test.txt", "r")
for x in f:
  print(x)


# 4) Use readlines(): readlines可以按照行的⽅式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每⼀行的数据为一个元素。
# Syntax:
  file.readlines(hint)   # Hint: Optional. If the number of bytes returned exceed the hint number, no more lines will be returned. 
                                  # Default value is  -1, which means all lines will be returned.

f = open("test.txt", "r")
l = f.readlines()

print(l)    # ['Hello! Welcome to demofile.txt\n', 'This file is for testing purposes.\n', 'Good Luck!']

# 5) 还可以这样:
with open("test.txt", 'r') as f:
    for i in f:
        print(i)
        
'''
-------------------------------------------------------------------------------------------------------------------------------------
'''
                            #####  4.Close files
# It is a good practice to always close the file when you are done with it.

f = open("test.txt", "r")
print(f.readline())
f.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

'''
-------------------------------------------------------------------------------------------------------------------------------------
'''
 