"""
                    < 3 > String 判断类型 方法 - Judgment String
1. string.isspace()     :  如果string中只包含空格, 则返回True
2. string.isdecimal()   :  如果string只包含数字则返回True, 全角数字
3. string.isdigit()     :  如果string只包含数字则返回True, 全角数字, (1), \u00b2
4. string.isnumeric()   :  如果string只包含数字则返回True, 全角数字, 汉字数字
5. string.isalpha()     :  如果string至少有一个字符并且所有字符都是字母则返回True
6. string.isalnum()     :  如果string至少有一个字符并且所有字符都是字母或数字则返回True
7. string.istitle()     :  如果string是标题化的(每个单词的首字母大写)则返回True
8. string.islower()     :  如果string中包含至少一个区分大小写的字符, 并且所有这些(区分大小写的)字符都是小写,则返回True
9. string.isupper()     :  如果string中包含至少一个区分大小写的字符, 并且所有这些(区分大小写的)字符都是大写,则返回True
10. string.isidentifier() : 判断指定字符串是不是合法的标识符
"""
#                   1. string.isspace()   : 判断空白字符
space_str = "  "
print(space_str.isspace())  # True
print("  a ".isspace())  # False
print("  \t\n\r".isspace())  # True

# --------------------------------------------------------------------------------------------------------------------
#                   2. string.isdecimal()   : 判断字符串是否只包含数字 全角数字
#                   3. string.isdigit()   : 判断字符串是否只包含数字 全角数字, (1), \u00b2
#                   4. string.isnumeric()   : 判断字符串是否只包含数字 全角数字, 汉字数字

num_str = "1"   # 当数字是1.1时,全部为False. 因为全都不能判断小数
print(num_str.isdecimal())  # True
print(num_str.isdigit())  # True
print(num_str.isnumeric())  # True

num_str = "(1)"  # 这是 unicode 字符串 : 也就是从键盘上无法直接输入,但可以通过一些其他的输入法,或者特殊的方式输入的字符串
# "\u00b2"   ²
print(num_str.isdecimal())  # False
print(num_str.isdigit())  # True
print(num_str.isnumeric())  # True

num_str = "一千零一"
print(num_str.isdecimal())  # False
print(num_str.isdigit())  # False
print(num_str.isnumeric())  # True

# ---------------------------------------------------------------------------------------------------------------------
#                  5. string.isalpha() : 判断string至少有一个字符并且所有字符都是字母
#                                      只能是字母,不能有别的
s = "abcABC"
s2 = "@adf21"
print(s.isalpha())  # True
print(s2.isalpha())  # False

# -------------------------------------------------------------------------------------------------------------------
#                  6. string.isalnum() :  判断string至少有一个字符并且所有字符都是字母或数字
#                                       只能是 字母或数字
s = "abcdAAS34"
s2 = "ABC abc #@"
print(s.isalnum())  # True
print(s2.isalnum())  # False

# --------------------------------------------------------------------------------------------------------------------
#                  7. string.istitle() : 判断string是标题化的(每个单词的首字母大写)
s = "Abc And You"
s2 = "Abd and you"
print(s.istitle())  # True
print(s2.istitle())  # False

# --------------------------------------------------------------------------------------------------------------------
#                  8. string.islower() : 判断string中的字母都是小写的
s = "hello how are you?@#"
s2 = "hello Hi"
print(s.islower())  # True
print(s2.islower())  # False

# --------------------------------------------------------------------------------------------------------------------
#                  9. string.isupper() : 判断string中的字母都是大写的

s = "hello How Are you?@#"
s2 = "HELLO HI#@"
print(s.isupper())  # False
print(s2.isupper())  # True

# --------------------------------------------------------------------------------------------------------------------
#                  10. string.isidentifier() : 判断指定字符串是不是合法的标识符
#   合法的标识符只能由 字母, 数字, 下划线 组成
s = "Hello_Python123"
s2 = "Hello, Python123"
print(s.isidentifier())  # True
print(s2.isidentifier())  # False
