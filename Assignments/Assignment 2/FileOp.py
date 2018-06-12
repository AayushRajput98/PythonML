import os
print("Enter the location where directory is to be created:  ")
Rootdir=input("   Root Directory: ")
Name=input("    Name: ")
dirPath=Rootdir+":\\"+Name
if not os.path.exists(dirPath):
    os.mkdir(dirPath)
    print("Directory created at the location: ",dirPath)
else:
    print("The directory already exists")
fileName=input("Enter the name of the file to be created in the '" + Name + "' directory: ")
while os.path.exists(dirPath +"\\" + fileName):
    print("The file Already exist, Enter another name")
    fileName=input()
f=open(dirPath +"\\" + fileName, "w")
print("'"+fileName+"' has been created in the directory '"+Name+"'")
content=input("Enter the data to be written in the file: ")
f.writelines(content)
f.close()