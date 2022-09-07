my_str = "hello world name my name is Peter"

#           <1>  Upper case: it returns the string in upper case
print(my_str.upper())

#           <2> Lower case:
print(my_str.lower())

#       <3> replace string: replaces a string with another string
#print(my_str.replace('name', 'apple'))
my_str = my_str.replace('name', 'apple')
print(my_str.replace('name', 'apple', 1))

#       <4>  my_str.split(, sub_strcount) : string     Split әдісі жақшадағы символға байланысты Стрингті бөліп тастап, листқа салады
result = my_str.split()
result = my_str.split('name', 1)
print(result)

