ls = ["apple", "banana", "cherry"]

with open("test.txt","w") as f:
    for i in ls:
        f.write("%s " %i)
