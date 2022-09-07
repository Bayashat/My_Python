with open("test2.txt", "w") as f:
    f.write("Test")
    f.seek(0)
    f.write("R")


with open("test.txt", "r") as rf:
    with open("test2.txt", "w") as wf:
        for line in rf:
            wf.write(line)

with open("test.txt", "a") as f:
    f.write("There are more contents")