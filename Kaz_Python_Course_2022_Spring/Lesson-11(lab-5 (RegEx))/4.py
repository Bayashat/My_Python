import re


# Apple Banana
str = input()

print(re.search(r"[A-Z][a-z]+", str))