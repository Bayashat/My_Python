import os

                         ####### 1) getcwd() 
                        # return current directory. 返回当前目录路径


print(os.getcwd())  # E:\KBTU\PP\Phyton\Week-6(Directories and files)

'''
-----------------------------------------------------------------------------------------------------------------------------------
'''
                        ####### 2) chdir()
                # Change the current working directory to the specified path.
                # 改变默认目录路径

# Syntax: os.chdir(Dname)   


os.chdir('Dir1')    # we changed to Dir1 folder 
# os.mkdir('Dir_1')   # and created that Dir_1 folder.

# let's back t our folder:
os.chdir('E:\KBTU\PP\Phyton\Week-6(Directories and files)')

'''
-----------------------------------------------------------------------------------------------------------------------------------
'''

                        ####### 3) listdir()
                    # gives us the list of folders in our path
                    # 获取目录列表
# 1.Syntax: 
    print(os.listdir('.'))      # ['0(file handing).py', '1(open-read file).py', '2(write-create file).py', 
                                #'3(delete file).py', '4(file methods).py', '5(directories).py', '6.py', 'Dir1', 'test.txt']


# 2.What happen if we changes our path to Dir1:
os.chdir('Dir1')

print(os.listdir('.'))  # ['Dir_1']

# 或者也可以直接在括号里写所需要的目录:
os.listdir("Dir1")  # ['Dir_1']

# let's back:
os.chdir('E:\KBTU\PP\Phyton\Week-6(Directories and files)')

# 3.Let's print out our folder's paths:
BASE_ULR = os.getcwd()
for target in os.listdir('.'):
    # target_path = BASE_ULR + '/' + target   # Not recommended
    target_path = os.path.join(BASE_ULR, target)
    print(target_path)      # E:\KBTU\PP\Phyton\Week-6(Directories and files)\0(file handing).py  ..... E:\KBTU\PP\Phyton\Week-6(Directories and files)\6.py .... 

# 4. 我们可以这样将folder 和 file 区分显示:
    if os.path.isfile(target_path):
        print(f"FILE: {target_path}")
    if os.path.isdir(target_path):
        print(f"DIR: {target_path}")
    ##   DIR: E:\KBTU\PP\Phyton\Week-6(Directories and files)\Dir1\Dir_1
    ##   FILE: E:\KBTU\PP\Phyton\Week-6(Directories and files)\6.py
'''
-----------------------------------------------------------------------------------------------------------------------------------
'''

                        ##### 4) walk(root,dirs,files)
                    ## For each directory in the directory tree rooted at top
# Syntax: 
    os.walk('.')

for root, dirs, files in os.walk('.'):
    print(root,dirs,files)

'''
. ['Dir1'] ['0(file handing).py', '1(open-read file).py', '2(write-create file).py', '3(delete file).py', '4(file methods).py', '5(directories).py', '6.py', 'test.txt']    
.\Dir1 ['Dir_1'] []
.\Dir1\Dir_1 [] []
'''

'''
-----------------------------------------------------------------------------------------------------------------------------------
'''

                                    ##### 5) mkdir("fname")
                    ### create a directory(folder): If exist , error. If does not exist , woluld create .
syntax: 
    os.mkdir("fname")

# 因为可能会报错,所以在创建前检查再create:
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

'''
-----------------------------------------------------------------------------------------------------------------------------------
'''

                                ##### 6) makedires("f1/f2/f3")
                                ## Create multiple dirs / create a leaf directory and all intermediate ones.
# Syntax : 
    os.makedirs("f1/f2/f3")

os.makedirs("Dir2/f1/f2")

'''
-----------------------------------------------------------------------------------------------------------------------------------
'''

                                ##### 7) rename("initial.txt", "ini_changed.txt")
                                ## Rename a file or directory. 重命名
                                # If there is no such file or dir, return error.
# Syntax:
    os.rename(f1,f1_chnange)

os.rename("test.txt", "test_change.txt")
os.rename("Dir1", "Dir_change.txt")

'''
-----------------------------------------------------------------------------------------------------------------------------------
'''

                                ##### 8) rmdir("dname")
                                ## remove dir
# Syntax:
    os.rmdir("dname")

os.rmdir("Dir1")