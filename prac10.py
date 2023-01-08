#Print the fibonacci sequence for the length given by the user as input
#using 'for' loop:
x=int(input())
n1=0
n2=1
for i in range(0,x):
    print(n1)
    n1,n2=n2,n1+n2

#using while loop:
x=int(input())
count=0
n1=0
n2=1
for i in range(0,x):
    print(n1)
    n1,n2=n2,n1+n2
    count+=1
