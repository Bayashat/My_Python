################  46.open()

'''
The open() function opens a file, and returns it as a file object.

# Syntax:
open(file, mode)

file	----    The path and name of the file
mode	-----   A string, define which mode you want to open the file in:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Open a file and print the content:

f = open("test.txt", "r")
print(f.read())

