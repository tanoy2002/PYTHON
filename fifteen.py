#Learning how try and except block works in Python(Exception Handling)
a=input("Enter a number: ")
b=input("Enter a number: ")
try:#try executing this block if proper inputs are given or enter the exception block
  print(int(a)+int(b))
except Exception as e:#After entering the except block print the error message as a separate line in the ouput #Exception is in Capital letters
  print(e)
print("This line plays a major role")#this line prints irrespective of whether the lines above run or not
################################
#if we dont use a try except block, the program will stop right at the point where the code is giving an error without printing the statements ahead of the error i.e, in short exiting the program
