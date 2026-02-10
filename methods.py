#types of methods
#instance methods
class student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('hi', self.name)
        print('your marks are', self.marks)
s1=student("arnav",600) 
s1.display()       

#accessor(getter) method and mutator(setter) method
class student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
s1=student()
s1.setname("jhon")
print(s1.getname())

class Student:
    def __init__(self, name):   # constructor
        self.name = name
    def setname(self, name):
        self.name = name
    def getname(self):
        return self.name
s1 = Student("John")     # Now this is valid
print(s1.getname())


#class methods
class bird:
    wings=2
    @classmethod
    def fly(cls, name):
        print(f"{name} flies with {cls.wings} wings")
bird.fly("sparrow")
bird.fly("pigeon")

#static method
class calculate:
    @staticmethod
    def add(x,y):
        return x+y
res=calculate.add(20,40)
print(res)
