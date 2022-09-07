#       <1>
'''
in python single quotation marks is same as double quotation marks


'hello'  ==  "hello"
'''

#     <2> Assign string to a variable
s = "hello"
print(s)


#     <3>  Multiple strings : using 3 quotes
b = """jsdffef jfsf rgkdfh  d g  h h h hhj  hhhj"""
print(b)

#       <4>  strings are arrays
a = "Hello world"
print(a[0])  # 'H'

#       <5>  lopping through a string
for i in "banana":
    print(i)

#       <6>  string length
print(len(a))   # 11

#          <7>  check
txt = "I love Almaty and Astana"
print("ppp" in txt)  #

#       <8>  use it in an if statement:
txt = "I love Almaty and Astana"

if "Astana" in txt:
    print("Oppps")
else:
    print("Yeahhhh!!!")

