"""
                        15. Residency Mechanism - 字符串的驻留机制
    * <1> 什么叫字符串驻留机制?
        - 仅保存一份相同且不可变字符串的方法, 不同的值被存放在字符串的驻留池中, Python的驻留机制对相同的字符串只保留一份拷贝, 后续创建
          相同字符串时, 不会开辟新空间, 而是把该字符串的地址赋给新创建的变量
"""
a = 'python'
b = "python"
c = '''python'''

print(a, id(a))  # python 1749051387248
print(b, id(b))  # python 1749051387248
print(c, id(c))  # python 1749051387248

"""
    * <2> 驻留机制的几种情况(交互模式):
        - 字符串的长度为 0 或 1 时
        - 符合标识符的字符串
        - 字符串只在编译时进行驻留, 而非运行时
        - [-5, 256] 之间的整数数字
        
"""
a = "abc%"
b = "abc%"
print(a is b)   # 是 False, 地址不一致
"""
    * <3> sys 中的 intern 方法强制两个字符串指向同一个对象
"""
a = -6
b = -6
print(a is b)  # 是 False, 地址不一致

import sys
a = a.intern(b)
print(a is b)  # 是 True, 强制开一个空间

"""
    * <4> Pycharm 对字符串进行了优化处理
"""
# 在 Pycharm, 都被进行优化了

