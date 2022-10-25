#if-else,elif workings
# a=50
# b=92
# c=int(input("Enter a number: "))
# if b>c:
#   print("The entered number is lesser")
# elif b==c:
#   print("The entered number is equal")
# else:
#   print("The entered number is greater")
# #checking the use of 'in' keyword
# list=[2,7,9,10,5,6,15]
# h=int(input("Enter your number: "))
# if h in list:
#   print(h,"is present in the list")
# else:
#   print(h,"is not present in the list")
# #second way of checking in which o/p is obtained in the form of either true or false
# print(7 in list)
# print(7 not in list)


###practice program on if else elif
a=int(input("Enter your age: "))
if a>150 or a<8:
  print("Invalid Age")
elif a>18:
  print("You are suitable for driving a car")
elif a==18:
  print("You are suitable for driving a car but we need to check on you personally")
else:
  print("You aren't suitable for driving a car")
