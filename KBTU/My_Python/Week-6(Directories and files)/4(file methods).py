############   Python has a set of methods available for the file object.

1) close()	                        Closes the file



2) detach()	            Returns the separated raw stream from the buffer


3) fileno()	        Returns a number that represents the stream, from the operating system's perspective

    f = open("test.txt", "r")
    print(f.fileno())   # 3


4) flush()	        Flushes the internal buffer

5) isatty()	        Returns whether the file stream is interactive or not

6) read()	        Returns the file content

7) readable()	    Returns whether the file stream can be read or not
        # The readable() method returns True if the file is readable, False if not.
        # Ex-1: Check if the file is readable:
    f = open("test.txt", "r")
    print(f.readable())

8) readline()	    Returns one line from the file

9) readlines()	    Returns a list of lines from the file


10) seek()	        Change the file position. 作⽤：⽤来移动文件指针.
        # Syntax: 文件对象.seek(偏移量, 起始位置)
        # 参数是2个0时可只写1个 : 表示不偏移,起始位置是0
        起始位置：
            0：文件开头
            1：当前位置
            2：⽂件结尾
    # 1. for r : 改变文件指针位置: 改变读取数据开始位置或把文件指针放结尾(让其无法读取数据).
    # 2. for a : 改变文件指针位置: 做到可以读取出来数据.

           ###### Test for r :
    f = open("test.txt", 'r')
    # 1)改变读取数据开始位置
    f.seek(2,0)  # 会从第儿个位置开始

    # 2) 把文件指针放结尾(让其无法读取数据).
    f.seek(0,2) 
    

        ##### Test for a :
    # a 改变文件指针位置: 做到可以读取出来数据:
    f.seek(0,0)

    con = f.read()
    print(con)
    f.close()


11) seekable()	    Returns whether the file allows us to change the file position

        #Check if the file is seekable:

    f = open("test.txt", "r")
    print(f.seekable())     # True


12) tell()	        Returns the current file position

    f = open("test.txt", "r")
    print(f.tell())     # 0


13) truncate()	    Resizes the file to a specified size
    # Open the file with "a" for appending, then truncate the file to 20 bytes:
    f = open("test.txt", "a")
    f.truncate(20)
    f.close()

    #open and read the file after the truncate:
    f = open("test.txt", "r")
    print(f.read())     # text 会被剪切


14) writable()	    Returns whether the file can be written to or not

    # f = open("demofile.txt", "a")
    print(f.writable())     # True


15) write()	        Writes the specified string to the file


16) writelines()	Writes a list of strings to the file

# Syntax : 
    file.writelines(list)

    # Open the file with "a" for appending, then add a list of texts to append to the file:

    f = open("test.txt", "a")
    f.writelines(["See you soon!", "Over and out."])
    f.close()

    #open and read the file after the appending:
    f = open("test.txt", "r")
    print(f.read())
