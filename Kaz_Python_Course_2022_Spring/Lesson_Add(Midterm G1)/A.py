import re

s = input()
if re.search(r"[A-Z][a-z]+", s):
    print("Found a match!")
else:
    print("Not matched!")