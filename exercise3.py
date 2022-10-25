n=18#number to be guessed
TG=9#maximum number of guesses allowed
NOG=0#Initial value for number of guesses
while(True):
    a=int(input("Enter a number: "))#user enters a number
    if a<n:
      print("Your number is smaller than expected")
      NOG=NOG+1#incrementing the value of number of guesses originally set to 0
      NOGL=TG-NOG##Number of guesses left
      if NOGL<1:
        print("Maximum no of guesses exceeded")
        break
      else:
        print("No. of guesses left: ",NOGL)


    elif a>n:
      print("Your number is greater than expected")
      NOG=NOG+1
      NOGL=TG-NOG
      if NOGL<1:
        print("Maximum no of guesses exceeded")
        break
      else:
        print("No. of guesses left: ",NOGL)
    else:
      print("You guessed the correct number")
      NOG=NOG+1
      NOGL=TG-NOG
      print("You guessed the correct number in no. of guesses: ",NOG)#no of guesses done is required not the no of guesses left
      break
