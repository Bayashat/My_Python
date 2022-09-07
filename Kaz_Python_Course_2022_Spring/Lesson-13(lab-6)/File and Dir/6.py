import  string

# print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

for i in string.ascii_uppercase:
    with open(i + ".txt", "w") as f:
        f.write(i)