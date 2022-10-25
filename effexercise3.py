n = 18
TG = 9
NOG = 0
while(True):
  a = int(input("Enter a number: "))
  NOG = NOG + 1
  NOGL = TG - NOG
  if a < n:
    print("Your number is smaller than expected")
    if NOGL < 1:
      print("Maximum no of guesses exceeded")
      break
    else:
      print("No. of guesses left: ", NOGL)

  elif a > n:
    print("Your number is greater than expected")
    if NOGL < 1:
      print("Maximum no of guesses exceeded")
      break
    else:
      print("No. of guesses left: ", NOGL)
  else:
    print("You guessed the correct number")
    print("You guessed the correct number in no. of guesses: ", NOG)
    break
