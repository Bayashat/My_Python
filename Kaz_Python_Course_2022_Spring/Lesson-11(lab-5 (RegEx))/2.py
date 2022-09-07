import re

str = input()  # abcd  ansbjas jabs cjas c

print(re.search(r"ab{2,3}", str))  # abb abbb