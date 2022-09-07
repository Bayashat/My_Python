import shutil

                                ######  1.rmtree("dname")
                                ## Recursively delete a directory tree
# Syntax:
    shutil.rmtree("dname")

shutil.rmtree("Dir1")

'''
-------------------------------------------------------------------------------------------------------------------------------------------------------
'''

                                ######## 2.move()
                                 ## Recursively move a file or directory to another location.Return the file or directory's destination.
# Syntax: 
    shutil.move()   

shutil.move("dir1/1.txt", "dir2/2.txt")

'''
-------------------------------------------------------------------------------------------------------------------------------------------------------
'''

                                ###### 3.copy("fname")
                                ## copy data, only for files.
# Syntax: 
    shutil.copy()

shutil.copy("dir1/1.txt", "dir2/2.txt")

'''
-------------------------------------------------------------------------------------------------------------------------------------------------------
'''

                                ##### 4.copytree()
                                 ## ecursively copy a directory tree and return the destination directory.
# Syntax:
    shutil.copytree()

shutil.copytree("Dir1", "Dir2")