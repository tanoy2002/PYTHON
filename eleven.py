# i=0
# while(True):
#   i=i+1
#   if i<5:
#     continue#directly move out of the loop
#   print(i,end=" ")
#   if i==45:
#     break#to stop the while loop at a given point
#
# a=0
# while(True):
#   a=a+15
#   if a<72:
#     continue
#   print(a+3,end=" ")
#   if a==300:
#     break




######Exercise : Take input from the user unless the number exceeds 100
while(True):
  b=int(input("Enter a number: "))#first we take input from the user within while loop
  if b<=100:
   continue#this statement returns back to the next iteration at line 24 where we are prompted to enter a number again
   print("Gorbachev")#since this statement is printed after continue it skips this and directly enters line 24 for a new iteration
  else:
    print("Congratulations, You have entered a number greater than 100")
    break#if we dont enter break command we will return to return to line 24 within while loop wherein we are prompted to enter a number again again


################################
#Some important points:
#while(True): is an infinite loop and runs as long as everything in the loop doesn't have a stopping condition(break)
#taking an input outside the while loop and satisfying a condition within the within the while(true) loop without a break statement leads to infinite loop
#in the above program the 24th statement gets printed multiple times prompting user for the input as long as the if condition is running
#as soon as the the else condition runs the break statements immediately ends the while(True): loop , failing to insert the break statement results in the line 24 prompting the user for inputs continuously(infinite loop)
#while(True): is specifically used when we want to take input from the user multiple times until a given condition is satisfied
