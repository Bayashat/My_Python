"""                 < 13 > String Methods

        (1) 判断类型
1. string.isspace()     :  如果string中只包含空格, 则返回True
2. string.isalpha()     :  如果string至少有一个字符并且所有字符都是字母则返回True
3. string.isalnum()     :  如果string至少有一个字符并且所有字符都是字母或数字则返回True
4. string.isdecimal()   :  如果string只包含数字则返回True
5. string.isdigit()     :  如果string只包含数字则返回True, 全角数字, (1), \u00b2
6. string.isnumeric()   :  如果string只包含数字则返回True, 全角数字, 汉字数字
7. string.istitle()     :  如果string是标题化的(每个单词的首字母大写)则返回True
8. string.islower()     :  如果string中包含至少一个区分大小写的字符, 并且所有这些(区分大小写的)字符都是小写,则返回True
9. string.isupper()     :  如果string中包含至少一个区分大小写的字符, 并且所有这些(区分大小写的)字符都是大写,则返回True

        (2) 查找和替换
1. string.startswith(str)   : 检查字符串是否以str开头,是则返回True
2. string.endswith(str)     : 检查字符串是否以str结束,是则返回True
3. string.find(str, start=0, end=len(string))   : 检测str是否包含在string中, 如果start和end指定范围, 则检查是否包含在指定范围内,
    如果是返回开始的索引值, 否则返回-1
4. string.rfind(str, start=0, end=len(string))  : 类似于 find() 函数, 不过是从右边开始查找
5. string.index(str, start=0, end=len(string))  : 跟 find() 方法类似, 只不过如果str不在string会报错
6. string.rindex(str, start=0, end=len(string)) : 类似于index(), 不过是从右边开始
7. string.replace(old_str, new_str, num=string.count(old)) : 把string中的old_str替换成new_str, 如果num指定, 则替换不超过num次

        (3) 大小写转换
1. string.capitalize()  : 把字符串的第一个字符大写
2. string.title()       : 把字符串的每个单词首字母大写
3. string.lower()       : 转换string中所有大写字符为小写
4. string.upper()       : 转换string中的小写字母为大写
5. string.swapcase()    : 翻转string中的大小写

        (4) 文本对齐
1. string.ljust(width)  : 返回一个原字符串左对齐, 并使用空格填充至长度width的新字符串
2. string.rjust(width)  : 返回一个原字符串右对齐, 并使用空格填充至长度width的新字符串
3. string.center(width) : 返回一个原字符串居中, 并使用空格填充至长度width的新字符串

        (5) 去除空白字符
1. string.lstrip()  : 截掉string左边(开始)的空白字符
2. string.rstrip()  : 截掉string右边(末尾)的空白字符
3. string.strip()   : 截掉string左右两边的空白字符

        （6） 拆分和连接
1. string.partition(str)    : 把字符串string分成一个3元素的元组(str前面, str, str后面)
2. string.rpartition(str)   : 类似于partition()函数, 不过是从右边开始查找
3. string.split(str="", num) : 以str为分隔符切片string, 如果num有指定值, 则仅分隔num+1个子字符串, str默认包含'\r', '\t', '\n' 和空格
4. string.splitlines()      : 按照行('\r','\n','\r\n')分隔, 返回一个包含各行作为元素的列表
5. string.join(seq) : 以string作为分隔符, 将seq中所有的元素(的字符串表示)合并为一个新的字符串


"""

# capitalize()	        Converts the first character to upper case
# casefold()	        Converts string into lower case
# center()	            Returns a centered string
# count()	            Returns the number of times a specified value occurs in a string
# encode()	            Returns an encoded version of the string
# endswith()	        Returns true if the string ends with the specified value
# expandtabs()	        Sets the tab size of the string
# find()	            Searches the string for a specified value and returns the position of where it was found
# format()	            Formats specified values in a string
# format_map()	        Formats specified values in a string
# index()	            Searches the string for a specified value and returns the position of where it was found
# isalnum()	            Returns True if all characters in the string are alphanumeric
# isalpha()	            Returns True if all characters in the string are in the alphabet
# isdecimal()	        Returns True if all characters in the string are decimals
# isdigit()	            Returns True if all characters in the string are digits
# isidentifier()	    Returns True if the string is an identifier
# islower()	            Returns True if all characters in the string are lower case
# isnumeric()	        Returns True if all characters in the string are numeric
# isprintable()	        Returns True if all characters in the string are printable
# isspace()	            Returns True if all characters in the string are whitespaces
# istitle()	            Returns True if the string follows the rules of a title
# isupper()	            Returns True if all characters in the string are upper case
# join()	            Joins the elements of an iterable to the end of the string
# ljust()	            Returns a left justified version of the string
# lower()	            Converts a string into lower case
# lstrip()	            Returns a left trim version of the string
# maketrans()	        Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

"""
1.capitalize()
将字符串的第一个字符转换为大写

2. center(width, fillchar)
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

3. count(str, beg= 0,end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

4. bytes.decode(encoding="utf-8", errors="strict")
Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。

5.encode(encoding='UTF-8',errors='strict')
以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

6. endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

7. expandtabs(tabsize=8)
把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

8.find(str, beg=0, end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

9.index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常。

10.isalnum()
如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False

11.isalpha()
如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False

12.isdigit()
如果字符串只包含数字则返回 True 否则返回 False..

13.islower()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

14.isnumeric()
如果字符串中只包含数字字符，则返回 True，否则返回 False

15.isspace()
如果字符串中只包含空白，则返回 True，否则返回 False.

16.istitle()
如果字符串是标题化的(见 title())则返回 True，否则返回 False
17.isupper()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

18.join(seq)
以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

19.len(string)
返回字符串长度

20.ljust(width[, fillchar])
返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

21.lower()
转换字符串中所有大写字符为小写.

22.lstrip()
截掉字符串左边的空格或指定字符。

23.maketrans()
创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

24.max(str)
返回字符串 str 中最大的字母。

25.min(str)
返回字符串 str 中最小的字母。

26.replace(old, new [, max])
把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。

27.rfind(str, beg=0,end=len(string))
类似于 find()函数，不过是从右边开始查找

28.rindex( str, beg=0, end=len(string))
类似于 index()，不过是从右边开始.

29.rjust(width,[, fillchar])
返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

30.rstrip()
删除字符串字符串末尾的空格.

31.split(str="", num=string.count(str))
以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串

32.splitlines([keepends])
按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

33.startswith(substr, beg=0,end=len(string))
检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

34.strip([chars])
在字符串上执行 lstrip()和 rstrip()

35.swapcase()
将字符串中大写转换为小写，小写转换为大写

36.title()
返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

37.translate(table, deletechars="")
根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中

38.upper()
转换字符串中的小写字母为大写

39.zfill (width)
返回长度为 width 的字符串，原字符串右对齐，前面填充0

40.isdecimal()
检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false

"""