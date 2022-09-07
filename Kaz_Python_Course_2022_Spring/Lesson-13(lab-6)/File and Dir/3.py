import os

path = input()  # D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS

if os.path.exists(path):

    print("\nfile name of the path: ")
    print(os.path.basename(path))  # KURS

    print("\nDir name of the path")
    print(os.path.dirname(path))  # D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python

else:
    print("No such path")