import os, os.path, time, shutil


def Over():
    print('''Do you want to continue?
    1 - YES
    2 - NO''')
    p  =input()
    if p == '1':
        Start_game()
    else:
        print("Good bye! See you next time!")

def Invalid():
    print("No such directory path")



def Rename_directory():
    print("what is the path of the directory?")
    a = input()
    if os.path.exists(a):
        os.chdir(a)

        print("please, enter the name of directory: ")
        b = input()

        if os.path.exists(b):
            if os.path.isdir(b):            
                print("please, enter the new name: ")
                c = input()
                os.rename(b,c)
            else:
                print("It's not a valid directory name")
                Over()
        else:
            print("No such directory")
            Over()

    else:
        Invalid()
        Over()


def Number_files():
    cnt = 0
    print("what is the path of the directory?")
    a = input()

    if os.path.exists(a):
        os.chdir(a)

        for files in os.listdir(a) :
           if os.path.isfile(files):
               cnt += 1
        print(f"The number of files is : {cnt}")  

        # or:
        '''
        cnt = len([file for file in os.listdir(a) if os.path.isfile(file)])
        '''

        print(cnt)
    else:
        Invalid()
        Over()


def Number_directories():
    cnt = 0
    print("what is the path of the directory?")
    a = input()

    if os.path.exists(a):
        os.chdir(a)

        for dirs in os.listdir(a) :
           if os.path.isdir(dirs):
               cnt += 1
        print(f"The number of directories is : {cnt}")  

        # or:
        '''
        cnt = len([file for file in os.listdir(a) if os.path.isdir(file)])
        '''

    else:
        Invalid()
        Over()


def List_of_content():
    print("what is the path of the directory?")
    a = input()

    if os.path.exists(a):
        os.chdir(a)

        for content in os.listdir(a) :
            print(content)

    else:
        Invalid()
        Over()

def Add_file():
    print("what is the path of the directory?")
    a = input()

    if os.path.exists(a):
        os.chdir(a)

        print("Please, enter the name of file which you want to create: ")
        b = input()
        if not os.path.exists(b):
            f = open(b,'x')
            f.close()
            print("Created successfully")
        else:
            print("Such file has already exists")
            Over()

    else:
        Invalid()
        Over()


def Add_dir():
    print("what is the path of the directory?")
    a = input()

    if os.path.exists(a):
        os.chdir(a)

        print("Please, enter the name of directory which you want to create: ")
        b = input()
        if not os.path.exists(b):
            os.mkdir(b)
            print("Created successfully")
        else:
            print("Such directory has already exists")
            Over()
    else:
        Invalid()
        Over()


def Del_dir():

    print("what is the path of the directory?")
    a = input()

    if os.path.exists(a):
        os.chdir(a)

        print("Please, enter the name of directory which you want to delete: ")
        b = input()
        if os.path.exists(b):
            os.rmdir(b)
            print("Deleted successfully")
        else:
            print("No such directory")
            Over()
    else:
        Invalid()
        Over


def Work_directory():
    print('''
    1- rename directory
    2- print number of files
    3- print number of directories
    4- list content of the directory
    5- add file to this directory
    6- add new directory to this directory
    7- Delete directory
    ''')

    command = input()

    if command == '1':
        Rename_directory()

    if command == '2':
        Number_files()

    if command == '3':
        Number_directories()
    
    if command == '4':
        List_of_content()

    if command == '5':
        Add_file()

    if command == '6':
        Add_dir()

    if command == '7':
        Del_dir()
    else:
        print("Invalid input")
        Over()


def Rename_file():

    print("what is the path of the file?")
    a = input()
    if os.path.exists(a):
        os.chdir(a)

        print("please, enter the name of file: ")
        b = input()

        if os.path.exists(b):
            print("Enter the new name: ")
            c = input()
            os.rename(b,c)
            print("Successfully renamed!")
            Over()
        else:
            print("No such file")
            Over()

    else:
        Invalid()
        Over()




def Add_content():
    print("what is the path of the file?")
    a = input()
    if os.path.exists(a):
        os.chdir(a)

        print("please, enter the name of file: ")
        b = input()

        if os.path.exists(b):
            f = open(b,'a')
            print("Please, enter the text which you want to add: ")
            p = input()
            f.write(p)
            f.close()
            print("Successfully added")
        else:
            print("No such file")
            Over()

    else:
        Invalid()
        Over()

def Rewrite_content():
    print("what is the path of the file?")
    a = input()
    if os.path.exists(a):
        os.chdir(a)

        print("please, enter the name of file: ")
        b = input()

        if os.path.exists(b):
            f = open(b,'w')
            print("Please, enter the text which you want to rewrite: ")
            p = input()
            f.write(p)
            f.close()
            print("Successfully rewrited")
        else:
            print("No such file")
            Over()

    else:
        Invalid()
        Over()

def del_file():
    print("what is the path of the file?")
    a = input()
    if os.path.exists(a):
        os.chdir(a)

        print("please, enter the name of file: ")
        b = input()

        if os.path.exists(b):
            os.remove(b)
            print("Successfully deleted!")
            Over()
        else:
            print("No such file")
            Over()

    else:
        Invalid()
        Over()


def Work_file():
    print('''
    1- rename file
    2- add content to this file
    3- rewrite content of this file
    4- delete file
    5- return to the parent directory
    ''')

    command = input()

    if command == '1':
        Rename_file()

    if command == '2':
        Add_content()

    if command == '3':
        Rewrite_content()
    
    if command == '4':
        del_file()

    if command == '5':
        Returnn()


def Start_game():
    print('''what do you want?
    -if work with directory press d oe D
    -if work with file press f or F
    ''')
    s = input()
    if s == ('d' or 'D'):
        Work_directory()
    elif s == ('f' or 'F'):
        Work_file()
    else:
        print("Invalid input")
        Over()

Start_game()