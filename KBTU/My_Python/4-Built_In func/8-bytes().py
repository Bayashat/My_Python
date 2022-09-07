############  8.bytes()
'''
The bytes() function returns a bytes object.

It can convert objects into bytes objects, or create empty bytes object of the specified size.

The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.
'''

# Syntax
bytes(x, encoding, error)

'''

x	        A source to use when creating the bytes object.
            If it is an integer, an empty bytes object of the specified size will be created.
            If it is a String, make sure you specify the encoding of the source.

encoding	The encoding of the string

error	    Specifies what to do if the encoding fails.

'''

'''
*********************************************************************************************************************
'''

## Ex-1: Return an array of 4 bytes:

x = bytes(4)    # b'\x00\x00\x00\x00'
