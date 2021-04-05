import os
import re

def Menu_of_files():
    print("OK, what next you want to do?")
    print("type 1 to delete file")
    print("type 2 to rename file")
    print("type 3 to add content to this file")
    print("type 4 to rewrite content of this file")
    print("type 5 to return to the parent directory")

def Menu_of_directory():
    print("OK, what next you want to do?")
    print("type 1 to rename directory")
    print("type 2 to print number of files")
    print("type 3 to print number of directories")
    print("type 4 to print list content of the directory")
    print("type 5 to add file to this directory")
    print("type 6 to add new directory to this directory")

print("Hello! You have opened \"File Manager\"")

while True:
    currentPath = os.getcwd()
    print("Your current path is: " + currentPath)
    choose = int(input("What you want to work with? Files or directory? Accordingly type 1, 2 or 3 to close program: "))
    if choose==3 :
        exit()
    elif choose==1:
        #Files
        Menu_of_files()
        choose1 = int(input())
        if choose1==1:
            #delete file
            File = input("Enter a file name that you want to delete: ")
            if os.path.exists(File + ".txt"):
                os.remove(currentPath + "/" + File + ".txt")
                print("Ok! File removed successfully!")
            else:
                print("Oh no! There is a problem! That file does not exist! You should type a name of file accurately or change directory!")
        elif choose1==2:
            #rename file
            File = input("Enter a file name that you want to rename: ")
            if os.path.exists(File + ".txt"):
                NewFile = input("Enter a new file name: ")
                os.rename(File + ".txt", NewFile + ".txt")
                print("Ok! File renamed successfully!")
            else:
                print("Oh no! There is a problem! That file does not exist! You should type a name of file accurately or change directory!")
        elif choose1==3:
            #add content to a file
            File = input("Enter a file name that you want to add some content: ")
            if os.path.exists(File + ".txt"):
                f = open(File + '.txt', 'a')
                text = input("Write a text that you want to append in \""+ File + "\": ")
                f.write(text)
                f.close()
                print("Ok! Text appended successfully!")
            else:
                print("Oh no! There is a problem! That file does not exist! You should type a name of file accurately or change directory!")
        elif choose1==4:
            #rewrite content
            File = input("Enter a file name that you want to rewrite content: ")
            if  os.path.exists(File + ".txt"):
                f = open(File + ".txt", 'w')
                text = input("Write a text that you want to rewrite in \""+ File + "\": ")
                f.write(text)
                f.close()
                print("Ok! Text rewrited successfully!")
        elif choose1==5:
            #return to the parent directory
            os.chdir("..")
            print("Ok! You returned to parent directory successfully!")
    elif choose==2:
        #directories
        Menu_of_directory()
        choose2 = int(input())
        if choose2==1:
            #rename directory
            NameOfDir = input("Enter the name of the directory that you want to rename: ")
            if os.path.exists(NameOfDir):
                NewDir = input("Enter the new name of this directory: ")
                os.rename(NameOfDir, NewDir)
                print("Ok! You renamed this directory successfully!")
            else:
                print("Oh no! There is a problem! That directory does not exist! You should type a name of file accurately or change directory!")
        elif choose2==2:
            #print number of files
            NameOfDir = input("Enter the name of the directory that you want to print number of files: ")
            if os.path.exists(NameOfDir):
                cnt = 0
                for i in os.listdir(NameOfDir):
                    x = re.fullmatch(r'.+\..+', i)
                    if x:
                        cnt += 1
                print(cnt,'that files you have in this directory')
            else:
                print("Oh no! There is a problem! That directory does not exist! You should type a name of file accurately or change directory!")
        elif choose2==3:
            #print number of directories
            NameOfDir = input("Enter the name of the directory that you want to print number of directories: ")
            if os.path.exists(NameOfDir):
                cnt = 0
                for i in os.listdir(NameOfDir):
                    x = re.fullmatch(r'.+\..+', i)
                    if not x:
                        cnt += 1
                print(cnt,"that directories you have in this directory")
            else:
                print("Oh no! There is a problem! That directory does not exist! You should type a name of file accurately or change directory!")
        elif choose2==4:
            #print content of this directory
            NameOfDir = input("Enter the name of the directory that you want to print content: ")
            if os.path.exists(NameOfDir):
                for i in os.listdir(NameOfDir):
                    print(i)
                print("That all files and directories!")
            else:
                print("Oh no! There is a problem! That directory does not exist! You should type a name of file accurately or change directory!")
        elif choose2==5:
            #add file to this directory
            NameOfDir = input("Enter the name of the directory that you want to add file: ")
            if os.path.exists(NameOfDir):
                NewFile = input("Enter a new file name that you want to create: ")
                f = open(NewFile + '.txt', 'w')
                f.close()
                print("OK! " + NewFile + ".txt maded successfully!")
            else:
                print("Oh no! There is a problem! That directory does not exist! You should type a name of file accurately or change directory!")
        elif choose2==6:
            NameOfDir = input("Enter the name of the directory that you want to add directory: ")
            if os.path.exists(NameOfDir):
                NewDir = input("Enter a new directory name that you want to create: ")
                if not os.path.isdir(NewDir):
                    os.mkdir(NewDir)
                    print("OK! New directory maded successfully!")
                else:
                    print("Error!")
                