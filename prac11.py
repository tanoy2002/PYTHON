


#Reversing a string
# def reverse_string(str):
#     str1 = ""   # Declaring empty string to store the reversed string
#     for i in str:
#         str1 = i + str1
#     return str1    # It will return the reverse string to the caller function

# str = "JavaTpoint"    # Given String
# print("The original string is: ",str)
# print("The reverse string is",reverse_string(str)) # Function call
# n1=6742
# minutes=n1//60
# hours=minutes//60
# minutes2=minutes-60
# print(hours,minutes2,seconds)
def converter(x):
    min1,sec=divmod(x,60)
    hrs,min1=divmod(min1,60)
    return "%d:%02d:%02d"%(hrs,min1,sec)
x=12345
print(converter(x))

# n=12345456555645
# sec=n%60
# min1=n//60
# hrs=min1//60
# min2=min1%60
# print(hrs,min2,sec)
# str1="This is a string"
# str2=str1.split(" ")
# print(" ".join(str2))
# def func1(a,b,*args):
#     mul=a*b
#     for num in args:
#         mul=mul*num
#     return mul
# print(func1(1,2,3,4,5))
# def func2(**kwargs):
#     for key,value in kwargs.items():
#         print(key+":",value)
# func2(argument1="arg1",argument2="arg2",argument3="arg3")
# class employee:
#     def __init__(self,e_name):
#         self.e=e_name
#     def introduce(self):
#         print("My name is: ",self.e)
# emp1=employee("Mr.X")
# print(emp1.e)
# emp1.introduce()
#single inheritance
# class Parentclass:
#     def parfunc(self):
#         print("This is the parent class")
# class Childclass(Parentclass):
#     def chfunc(self):
#         print("This is the child class")
# obj1=Childclass()
# obj1.parfunc()
# obj1.chfunc()
# #multilevel inheritance
# class Parentclass:
#     def parfunc(self):
#         print("This is the parent class")
# class Childclass(Parentclass):
#     def chfunc(self):
#         print("This is the child class")
# class Childclass2(Childclass):
#     def chfunc2(self):
#         print("This is the second child class")
# obj1=Childclass2()
# obj1.parfunc()
# obj1.chfunc()
# obj1.chfunc2()
#multiple inheritance
# class Parentclass1:
#     def parfunc(self):
#         print("This is the parent class 1")
# class Parentclass2:
#     def parfunc2(self):
#         print("This is the parent class 2")
# class Childclass(Parentclass1,Parentclass2):
#     def chfunc2(self):
#         self.parfunc()
#         self.parfunc2()
# obj1=Childclass()
# obj1.chfunc2()
#checking for child is inherited and for checking whether object is an is instance
class parent:
    pass
class child(parent):
    pass
print(issubclass(child,parent))
print(issubclass(parent,child))
obj1=child()
obj2=parent()
print(isinstance(obj2,child))
print(isinstance(obj2,parent))
