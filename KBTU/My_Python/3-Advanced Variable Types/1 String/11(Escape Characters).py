"""                     <11> Escape Character - 转义字符
 * To insert characters that are illegal in a string, use an "ESCAPE CHAR"

 * An "ESCAPE CHAR" is a backslash \ followed by the character you want to insert.

 * The escape character allows you to use double quotes when you normally would not be allowed:
"""
txt = "We are the so-called \"Vikings\" from the north."  # We are the so-called "Vikings" from the north.

# Other escape characters used in Python:
"""
        (1)    \(在行尾时)	        续行符

>>> print("line1 \
    line2 \
    line3")
#   line1     line2     line3

        (2)     \\      反斜杠符号 - Backslash
>>> print("\\")
#   \

        (3)     \'	    单引号 - Single Quote
>>> print('\'')
#   '

        (4)     \"	    双引号
>>> print("\"")
#   "

        (5)     \a	    响铃

>>> print("\a")
#   执行后电脑有响声。

        (6)     \b	    退格(Backspace)
>>> print("Hello \b World!")
#   Hello World!

        (7)     \000	空
>>> print("\000")
>>>

        (8)     \n	    New Line - 换行
>>> print("\n")


        (9)     \v	    纵向制表符
>>> print("Hello \v World!")
Hello
       World!

        (10)    \r	     Carriage Return    \r	回车,将 \r 后面的内容移到字符串开头,并逐一替换开头部分的字符,
                直至将 \r 后面的内容完全替换完成
>>> print("Hello\rWorld!")
#   World!
>>> print('google runoob taobao\r123456')
#   123456 runoob taobao

        (11)    \t	    Tab   横向制表符
>>> print("Hello \t World!")
#   Hello      World!

        (12)    \f	    Form Feed   换页
>>> print("Hello \f World!")
Hello
       World!

        (13)    \yyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。	
>>> print("\110\145\154\154\157\40\127\157\162\154\144\41")
#   Hello World!

        (14)    \xyy	十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
>>> print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
#   Hello World!


        (15)    \ooo	        Octal value  十进制数

"""

