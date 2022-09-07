with open("test.txt", "r") as f1:
    with open("test2.txt", "w") as f2:
        for content in f1:
            f2.write(content)