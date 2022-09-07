import os

path = input()
print("Exist", os.access(path, os.F_OK))

print("Readble", os.access("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-13(lab-6)\File and Dir", os.R_OK))

print("Writable", os.access("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-13(lab-6)\File and Dir", os.W_OK))

print("Executable", os.access("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-13(lab-6)\File and Dir", os.X_OK))


