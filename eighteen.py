f=open("exm2.txt","w")#now using w for write mode since it is not by default
f.write("This is a file for testing writing operations")
f.close()

f=open("exm2.txt","a")#now using a for append mode since it is not by default
f.write("This is a file for testing writing operations\n")
f.close()

###f.write() function returns the number of characters in the file, it is illustrated below
f=open("exm2.txt","w")
a=f.write("This is a file for testing writing operations\n")#storing the number of characters in the file in a variable
print(a)#printing the number of characters in the file
f.close()


################################################################
#Handle read and write at the same time
f=open("exm2.txt","r+")#r+ used for handling read and write at the same time
print(f.read())
f.write("This file is now adding a new line")
print(f.read())
