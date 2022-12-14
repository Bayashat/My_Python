"""
                < 10 > Compare String - 字符串的比较操作
* 运算符 : > >= < <= = == !=

* 比较规则 : 首先比较两个字符串中的第一个字符串, 如果相等则比较下一个字符, 依次比较下去, 直到两个字符串中的字符不相等时,
            比较结果就是两个字符串的比较结果, 两个字符串中的所有后续字符将不再被比较

* 比较原理 : 两个字符进行比较时, 比较的是其 ordinal value(原始值), 调用内置函数ord可以得到指定字符的ord value.
            与内置函数ord对应的是内置函数chr, 调用内置函数chr时指定ord value 可以得到其对应的字符
"""
print("apple" > "app")  # True
print("apple" > "ban")  # False : ord('a) < ord('b')


