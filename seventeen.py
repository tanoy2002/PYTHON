#Learning different ways of reading a file
f=open("exm.txt","r")#normal mode
a=f.read()
print(a)

f=open("exm.txt","rt")#default mode
a=f.read()
print(a)

f=open("exm.txt","rb")#binary mode
a=f.read()
print(a)

f=open("exm.txt")#normal mode
a=f.read(3)#reads first 3 characters
print(a)
a=f.read(5)#reads next 5 characters(only if same variable is used for intialization)
print(a)
a=f.read(34555)#reads the max no of characters because the value is huge
print("1",a)
a=f.read(34555)#there is nothing to read left in the file hence it prints only "2" in the o/p
print("2",a)

f=open("exm.txt")
for line in f:
  print(line,end="")#prints lines without \n or newline character

f=open("exm.txt")
print(f.readline())#for printing a single line one by one
print(f.readline())
print(f.readline())

f=open("exm.txt")
print(f.readlines())#prints all the lines as a list

f.close()#after a file is opened closing it is necessary
