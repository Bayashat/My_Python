with open("dog.jpg", "rb") as rf:
    with open("dog_copy2.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)

        