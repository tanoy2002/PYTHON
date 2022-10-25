class employee:#creating a clas
    def __init__(self,emp_name):
        self.e=emp_name#e is the attribute of the class
    def introduce(self):#introduce here is acting as a method of the class
        print("Hi My name is: "+self.e)

e1=employee("Mr.interview")
print(e1.e)
e2=employee("Mr.goo")
print(e2.e)
e2.introduce()
e1.introduce()

#inheritence
class parent_class:
  def par_func(self):
    print("Hi this is parent class")
class child_class(parent_class):
  def child_func(self):
    print("Hi this is child class")
obj1=child_class()
obj1.par_func()
obj1.child_func()
