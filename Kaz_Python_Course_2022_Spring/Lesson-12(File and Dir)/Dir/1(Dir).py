import os


            ############## 1) getcwd() : return the current location

print(os.getcwd())  # D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-12(File and Dir)\Dir


            ############### 2) chdir() : change thee directory 
os.chdir("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-5")
print(os.getcwd())
os.mkdir("am I in the right folder")

os.chdir("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS\Lesson-12(File and Dir)\Dir")

            ###########  3) listdir() : return the dirs that in the current location:
print(os.listdir())

os.chdir("D:\OneDrive - АО Казахстанско-Британский Технический Университет\My_Computer_User\JOB(E)\Programming\Python\KURS")
print(os.listdir())

            ############ 4) mkdir("dir_name") : make a new dir
os.mkdir("This is a test")

            ########### 5) makedirs("f1/f2/f3"): make multiple dirs
os.makedirs("f1/f2/f3")

            ##########   6) rename("initial_text", "new_name")
# os.rename("kbtu.txt", "Muit.txt")]


            ########   7) rmdir("dir_name") : Attentaion : only empty dir can be removed
os.rmdir("This is a test")
