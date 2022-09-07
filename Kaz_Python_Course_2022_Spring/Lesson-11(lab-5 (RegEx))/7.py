'''
snake case string : i_got_intern_at_geeksforgeeks
camel case string : IGotInternAtGeeksforgeeks
'''
import  re

str = input() # i_got_intern_at_geeksforgeeks

str = re.findall(r"[a-z]+", str) # ['i', 'got', 'intern', 'at', 'geeksforgeeks']

for i in range(len(str)):  # 0~4 : 5
    str[i] = str[i].capitalize()
print(str)  # ['I', 'Got', 'Intern', 'At', 'Geeksforgeeks']

print("".join(str)) # IGotInternAtGeeksforgeeks

'''
camel = ""

for x in snake.split("_"):
    camel += x.capitalize()

print(camel)
'''
