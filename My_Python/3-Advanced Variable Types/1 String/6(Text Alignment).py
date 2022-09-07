"""
                                < 6 > 文本对齐 - Text alignment
1. string.ljust(width, fill_char)  : 返回一个原字符串左对齐, 并使用fill_char填充至长度width的新字符串
2. string.rjust(width, fill_char))  : 返回一个原字符串右对齐, 并使用fill_char填充至长度width的新字符串
3. string.center(width, fill_char)) : 返回一个原字符串居中, 并使用fill_char填充至长度width的新字符串
4. string.zfill(width) : 返回一个原字符串居中, 并使用0填充至长度width的新字符串

"""
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

#                          (1) string.center(width, fill_char))
# 要求: 顺序并且居中对齐输出以下内容
for poem_str in poem:  # |   登鹳雀楼   |
    print("|%s|" % poem_str.center(10))  # |   王之涣    |
    #       |  白日依山尽   |
    #       |  黄河入海流   |
    #       |  欲穷千里目   |
    #       |  更上一层楼   |

s = "hello,python"
print(s.center(20, "*"))    # ****hello,python****

# ------------------------------------------------------------------------------------------------------------------
#                           (2)  string.ljust(width, fill_char)

for poem_str in poem:  # |登鹳雀楼      |
    print("|%s|" % poem_str.ljust(10))  # |王之涣       |
    #      |白日依山尽     |
    #      |黄河入海流     |
    #      |欲穷千里目     |
    #      |更上一层楼     |

# -------------------------------------------------------------------------------------------------------------------
#                           (3) string.rjust(width, fill_char)

for poem_str in poem:  # |      登鹳雀楼|
    print("|%s|" % poem_str.rjust(10))  # |       王之涣|
    #     |     白日依山尽|
    #     |     黄河入海流|
    #     |     欲穷千里目|
    #     |     更上一层楼|

# -------------------------------------------------------------------------------------------------------------------
#                           (4) string.zfill(width)
s = "hello,python"
print(s.zfill(20))  # 00000000hello,python









