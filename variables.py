#instance variables
class car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
c1=car("honda", "civic")
c2=car("tata", "tiago")
print(c1.brand)
print(c1.brand)
print(c1.model)
print(c2.model)

#class variables
class car:
    wheels=4
    def __init__(self, brand):
        self.brand=brand
c1=car("honda")
c2=car("hyundai")
print(c1.wheels)
print(c2.wheels)
car.wheels=6
print(c1.wheels)
print(c2.wheels)

#local variables
class calculator:
    def add(self, a, b):
        c=a+b
        print(c)
    def multiply(self, a, b):
        c=a*b
        print(c)
x=calculator()
x.add(10, 20)
x.multiply(6, 6)