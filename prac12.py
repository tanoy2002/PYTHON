#hcf technique 1
a=int(input())
b=int(input())
c=int(input())
list1=[]
list2=[]
list3=[]
list4=[]
for i in range(1,a+1):
    if a%i==0:
        list1.append(i)
for i in range(1,b+1):
    if b%i==0:
        list2.append(i)
for i in range(1,c+1):
    if c%i==0:
        list3.append(i)
for x in list1:
    if x in list2 and list3:
        list4.append(x)
print(max(list4))
#LCM calculation
n1=int(input())
n2=int(input())
n3=int(input())
for i in range(max(n1,n2,n3),1+(n1*n2*n3)):
    if i%n1==i%n2==i%n3==0:
        lcm=i
        break
print(lcm)
#hcf technique 2
for i in range(1,max(n1,n2,n3)):
    if n1%i==n2%i==n3%i==0:
        hcf=i
print(hcf)
