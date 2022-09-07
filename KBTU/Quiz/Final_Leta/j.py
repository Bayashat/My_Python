import re

s = input()

x = re.search("^[p|P][p|P]2.*[m|M][i|I][d|D][t|T][e|E][r|R][m|M]$",s)
if x == None:
    print("No")
else:
    print("Success")