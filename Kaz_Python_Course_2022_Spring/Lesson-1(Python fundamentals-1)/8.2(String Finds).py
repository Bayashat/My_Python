my_str = "hello world name my name is Peter"


#           <1>     Find:   if doesn't found it, return -1
# formula : my_str.find(sub_str, start, end)

print(my_str.find("hello")) # 0
print(my_str.find('name')) # 12

print(my_str.find("hello", 3))  # -1

#           <2>    rfind() : right find
print(my_str.rfind('name'))  # 20


#           <3> index : same as find(), if doesn't found, it will return error
#print(my_str.index('apple'))

#           <4>  count(sub_str, start, end)
print(my_str.count('aaaaa')) # 0
print(my_str.count("name")) # 2
print(my_str.count('name', 13))  # 1