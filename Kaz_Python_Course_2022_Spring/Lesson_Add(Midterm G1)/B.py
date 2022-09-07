import re

s = input()

if re.search(r"^[\w]+$", s):
    print("Found a match!")
else:
    print("Not matched!")

