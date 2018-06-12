import os;
#Creating and writing in a file
f=open("F:\\ABC.txt","w")
f.writelines("Hello! I am writing this using python")
f.close()

#reading the file
f=open("F:\\ABC.txt","a")
f.writelines("This is the use of append function")
f.close()

#using os
os.remove("F:\\ABC.txt")  #Deleting the file

f=open("F:\\XYZ.txt","w")
f.writelines("Renamed files")
f.close()
#os.rename("F:\\XYZ.txt","F:\\Renamed file.txt")  #Renaming the file

print(os.getcwd()) #Fetching the current directory

#os.mkdir("F:\\SIP") #Creating a directory

#os.rmdir("F:\\SIP") #Removing the directory (If file exist remove the file first)

f=open("F:\\XYZ.txt","r+")
print(f.read(5))
f.close()

print(os.path.isfile("F:\\xyz"))

