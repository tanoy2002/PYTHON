#Program to print astrologer's stars in positive direction and in negative direction
a=int(input("Enter number of rows: "))
b=int(input("Enter 0 or 1:"))
c=bool(b)
if c==True:
  for i in range(1,a+1):
    print("*"*i)
else:
  for i in range(a,0,-1):
    print("*"*i)

#in line 4 we see the range is specified from (1 to a+1)
#(1 to a+1) simply means we want the smallest number or value that can be printed as 1
#whenever we take say a input as a=7 we want the loop to run for 7 rows but if we specify the range as (1,7) or (1,a) the loop will run for a-1 rows or 7-1=6 rows only
#Hence we add 1 to the extreme range to get the exact range to be printed
#Say we want to print range for numbers from 3 to 5 then we use (3,6),where 3 is included and 6 is excluded and hence the loop runs for 3,4 and 5
#the same goes for the else staatement printed above:
#say we want to print numbers from 5 to 1 we will write the range as (5,0,-1), where 5 is included and 0 is excluded and loop runs for 5,4,3,2,1. The -1 at the end is necessary as it will print the numbers in reverse order or else it will print everything as it is

#Space separated stars
a=int(input("Enter number of rows: "))
b=int(input("Enter 0 or 1:"))
c=bool(b)
if c==True:
  for i in range(1,a+1):
    print("* "*i)
else:
  for i in range(a,0,-1):
    print("* "*i)
