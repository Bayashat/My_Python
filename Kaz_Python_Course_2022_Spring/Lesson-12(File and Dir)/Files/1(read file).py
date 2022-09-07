'''
f = open("dir of our file", "mode")

type of modes:

1. "r" : read : Тек оқу үшін
2. "w": Write : берілген текстті толықтай өзгерді
3. "a"   берілген тексттің артына қоса мәлімет жазады

f.read()

f.close()

'''

        # 1. 
# f = open("test.txt", "r")

'''
print(f.name)  # test.txt
print(f.mode)  # r
'''
# print(f.readlines())

'''
print(f.readline())
print(f.readline())
print(f.readline())
'''
# f.close()

        # 2. with keyword
with open("test.txt", "r") as f:
    # print(f.read(10)) # Hello Worl

    size_to_read = 20
    content = f.read(size_to_read)
    while(len(content)) > 0:
        print(content, end = '*')
        content = f.read(size_to_read)



f = open("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\kbtu.txt", "r")
for i in f:
    print(i, end = "")
f.close()
print("**************************************************************")


with open("test.txt", "r") as f:
    size = 10
    content = f.read(10)
    print(content, end = "") # Hello Worl

    # print(f.tell()) 10
    f.seek(0)
    
    content = f.read(10)
    print(content, end = "") # Hello Worl