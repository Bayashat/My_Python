########### 7. bytearray()

'''
The bytearray() function returns a bytearray object.

It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
''' 
# Syntax:
bytearray(x, encoding, error)

'''
1. x	    A source to use when creating the bytearray object.
            If it is an integer, an empty bytearray object of the specified size will be created.
            If it is a String, make sure you specify the encoding of the source.

2. encoding	    The encoding of the string

3. error	    Specifies what to do if the encoding fails.

'''

'''
*********************************************************************************************************************
'''

## Ex-1: Return an array of 4 bytes:

x = bytearray(4)    # bytearray(b'\x00\x00\x00\x00')