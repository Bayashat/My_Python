import os

                    #######     1) Create a directory(folder): If exist , error. If does not exist , woluld create .
syntax: 

os.mkdir(fname)

# 因为可能会报错,所以在创建前检查:
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


1) os.path.isfile(f_name)      return whether that is a file or not.

2) os.path.isdir(f_name)      return whether that is a directory(folder) or not.

3) 删除directory(folder) :
if os.path.exists(directory_name):
    os.rmdir(directory_name)    # remove directory