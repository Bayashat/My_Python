"""
                    <12> decoding and encoding - 编码与解码
编码: s.encode(encoding="format")
解码: s.decode(encoding="format")

编码结果会是 byte, 也就是 二进制数据(字节类型的数据)
"""

#  1. 编码
s = "天涯共此时"
print(s.encode(encoding="GBK"))  # 在GBK这种编码格式中, 一个中文占两个字节
# b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'


print(s.encode(encoding="UTF-8"))  # 在UTF-8这种编码格式中, 一个中文占3个字节
# b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'

# ---------------------------------------------------------------------------------------------------------------------
# 2. 解码
byte = s.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))  # 天涯共此时

byte = s.encode(encoding="utf-8")
print(byte.decode(encoding="utf-8"))  # 天涯共此时










