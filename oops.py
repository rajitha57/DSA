# #creation of class and object
class greeting:
    def hello(self):
        print("welcome to oops")
x=greeting()
x.hello()

# #program to create student class and create an object to it
class student:
    def details(self):
        self.name= 'Rajitha'
        self.age=20
        self.branch='cse'
        self.marks=100
    def display(self):
        print(f"Hi, My name is:{self.name}")
        print(f"My age is: {self.age}")
        print(f"I am from {self.branch} branch")
        print(f"My marks are:{self.marks}")
s1=student()
s1.details()
s1.display()

#constructors
#Default constructors
class example:
    def __init__(self):
      print("constructor is called")
x=example()

#parameterized constructors
class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name}, Age:{self.age}")
s1=student("Rajitha", 20)
s1.display()
s2=student("RAJ", 10)
s2.display()

#Destructor
class example:
    def __init__(self):
        print("constructor is called")
    def __del__(self):
        print("destructor is called")
obj=example()
del obj

