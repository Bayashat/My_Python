# AppleBananaCherry  :  Apple Banana Cherry

# ABC : A B C
import re

str = input()
print(re.findall(r"[A-Z][a-z]*", str))