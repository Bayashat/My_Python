"""
                    < 7 >  去除空白字符 - Remove Whitespace

1. string.lstrip()  : 截掉string左边(开始)的空白字符
2. string.rstrip()  : 截掉string右边(末尾)的空白字符
3. string.strip()   : 截掉string左右两边的空白字符

"""
poem = ["   Болыс болдым мінеки  \t",
        "\n\tБар малымды шығындап  ",
        "  Түйеде қом, атта жал \n",
        "\t\nҚалмады елге тығындап  \t"]

for poem_str in poem:
        print("|%s|" % poem_str.lstrip())               # |Болыс болдым мінеки  	|
                                                        # |Бар малымды шығындап  |
                                                        # |Түйеде қом, атта жал
                                                        # |
                                                        # |Қалмады елге тығындап  	|
for poem_str in poem:
        print("|%s|" % poem_str.rstrip())               # |   Болыс болдым мінеки|
                                                        # |
                                                        #     Бар малымды шығындап|
                                                        # |  Түйеде қом, атта жал|
                                                        # |
                                                        # Қалмады елге тығындап|

for poem_str in poem:
        print("|%s|" % poem_str.strip())               # |Болыс болдым мінеки|
                                                       # |Бар малымды шығындап|
                                                       # |Түйеде қом, атта жал|
                                                       # |Қалмады елге тығындап|