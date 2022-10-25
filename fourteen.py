#Understang how functions work
a= 7
b=3
print(sum((a,b)))#in built function for calculating sum(something like a tuple/list is used for iterability)
def function1():
  print("Hello you are in function 1")
function1()#can be used to call a function which results in printing of the statements within the function
def function2(a,b):
  print("Hello you are in function 1",a+b)
function2(9,15)#can be used to call a function which results in printing of the statements within the function
def function3(a,b):
  """This is a function which calculates average of two numbers""" #This is a docstring which means that we can use this whenever we want to know what we have used a function for
  average=(a+b)/2
  return average
print(function3(9,15))
#or
v=function3(9,15)#second method
print(v)
print(function3.__doc__)#used to call the docstring of the function to understand what we used the function in the first place for
