import os

def traverse(dirName):
    for i in os.listdir(dirName):
        if os.path.isfile(dirName+"\\"+i):
            os.remove(dirName+"\\"+i)
        else:
            traverse(dirName+"\\"+i)
    os.rmdir(dirName)

'''Deleting a directory, along with its content'''

def del_dir():
    dirName=input("Enter the ROOT DIRECTORY to be scanned:  ")+":"
    for i in os.listdir(dirName):
        print(i)
    cd = input("Enter the sub-directory which is to be deleted:  ")
    while not cd is "":
        subPath="\\"+cd
        cd=input("Enter the sub-directory which is to be deleted:  ")
    traverse(dirName+subPath)
    print("The directory has been deleted")

'''Creating a directory'''

def init_dir():
    dirName = input("Enter the ROOT DIRECTORY: ") + ":"
    subdir = input("SUBDIRECTORY:  ")
    subpath = ""
    while not subdir is "":
        subpath += "\\" + subdir
        if not os.path.exists(dirName + subpath):
            os.mkdir(dirName+subpath)
        subdir = input("SUBDIRECTORY:  ")
    return dirName + subpath

'''Creating a file'''

def init_file():
    subDirPath=init_dir()
    fileName=input("Enter the name of the file to be created:  ")
    while os.path.exists(subDirPath+"\\"+fileName):
        fileName=input("File name already exists, Enter another name:  ")
    dirPath = subDirPath + "\\" + fileName
    f=open(dirPath,"w")
    content=input("Enter the content to be added in the file:  ")
    f.writelines(content)
    f.close()
    print("File has been created at the location: ",dirPath)

'''Reading a file'''

def read_file():
    subDir=init_dir()
    for i in os.listdir(subDir):
        print(i)
    fileName=input("Enter the file to be read: ")
    f=open(subDir+"\\"+fileName,"r")
    print(f.read())
    f.close()
    return subDir+"\\"+fileName
'''To append text in a file'''

def add_file():
    dirPath=read_file()
    f=open(dirPath,"+a")
    content=input("Enter the content to be appended")
    f.writelines(content)
    f.close()


print("Hello user! Welcome to DIRECTORY SCAN. Enter one of the following choices:")
condition="something"
while(not condition == ""):
    print("1. Create a Directory")
    print("2. Create a File")
    print("3. Delete a Directory")
    print("4. Read a file")
    print("5. Append text in a file")
    choice=int(input())
    try:
        if(choice==1):
            init_dir()
        elif(choice==2):
            init_file()
        elif(choice==3):
            del_dir()
        elif choice==4:
            uless=read_file()
        elif choice==5:
            add_file()
        else:
            print("Wrong Chocie")
    except:
        print("Something went wrong please try again")
    print("Press ENTER to quit")
    condition=(input())
print("Thankyou!!")