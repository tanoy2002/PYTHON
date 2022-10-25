#design a faulty calculator that returns wrong values for a given pair of inputs and a specific operation
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=input("Choose a math operator(+,-,/,*): ")
if a==45 and b==3 and c=="*":
  print(555)
elif a==56 and b==9 and c=="+":
  print(77)
elif a==56 and b==4 and c=="/":
  print(4)
elif c=="*":
  print(a*b)
elif c=="+":
  print(a+b)
elif c=="/":
  print(a/b)
else:
  print(a-b)
