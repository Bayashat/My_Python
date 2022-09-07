################    2. File write

                ####  1) Write to an Existing File

# To write to an existing file, you must add a parameter to the open() function:
# 不管是 a 还是 w 方式打开文件，写内容都是使用 write() 函数.

"a" - Append - will append to the end of the file 追加.若文件不存在,新建文件. 如果执行写入,在原有内容基础上,追加新内容.指针会在文件末尾.

"w" - Write - will overwrite any existing content. 只写.若文件不存在,新建文件.如果执行写入,会覆盖内容.

'''
-------------------------------------------------------------------------------------------------------------------
'''

        ##### Ex-1: Open the file "test.txt" and append content to the file:

f = open("test.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())

         #####  Ex-2: Open the file "test.txt" and overwrite the content:

f = open("test.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())

'''
-------------------------------------------------------------------------------------------------------------------
'''

                                        2) Create a New File
## To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist


        #### Ex-1: Create a file called "myfile.txt":

f = open("myfile.txt", "x")
# Result: a new empty file is created!

        #### Ex-2 : Create a new file if it does not exist:

f = open("myfile.txt", "w")