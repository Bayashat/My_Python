#               <1> str[start : end]
b = "Hello world"
print(b[2:5])  # llo

#           <2>  Slice from the start : str[:end]

print(b[:5])  # Hello

#           <3> Slice to the end  :  str[start:]
print(b[2:])  # llo world

#           <4> Negative indexing:
print(b[-5 : -2]) # wor

#       <5> Reverse string
print(b[::-1])      # dlrow olleH

#       <6>  Get the string itself

a = b[:]
print(a)