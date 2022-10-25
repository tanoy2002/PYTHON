#check whether a number is prime or not
x=int(input())
for i in range(2,x):
    if x%i==0:
        print("is not a prime")
        break
else:
    print("is a prime no")
