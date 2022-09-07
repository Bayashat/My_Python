##################  42.memoryview()

'''
The memoryview() function returns a memory view object from a specified object.

# Syntax: 
memoryview(obj)

obj     ----    A Bytes object or a Bytearray object.

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Create and print a memoryview object:

x = memoryview(b"Hello")

print(x)    # <memory at 0x03348FA0>

#return the Unicode of the first character
print(x[0]) # 72

#return the Unicode of the second character
print(x[1]) # 101