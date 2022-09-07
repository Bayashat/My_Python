import re

str = input()  # AbcDeje  : Abc Deje

str = re.sub(r"([a-z])([A-Z])", r"\1 \2", str)
print(str)