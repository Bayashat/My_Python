import re

str = input()  # abcd  ansbjas jabs cjas c : a ab abb abbb abbbbb

print(re.search(r"ab*", str))

'''
p = re.compile(r"ab*")  # a ab abbb abb
print(p.search(str))
'''
