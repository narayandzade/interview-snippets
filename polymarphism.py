#polymarphism is core concept of object-oriented programming . it allow to use same methods or functions perform diff diff functionality . it heps to reuse the code
#there are three way achive these concept in python
#1. Method overridnig with inhiritance
#2. method overloading using *args and **kwargs
#3. operator overloading using maigc or dunder method
from idlelib.pyshell import ModifiedUndoDelegator


#1. method overrridng using class inhiritance
class A:
    def show(self):
        print("Class A")
class B:
    def show(self):
        print("Class B")
class C (A, B):
    def show(self):
        print("Class C")

shows = (A(), B(), C())

for obj in shows:
    obj.show()


#2. method overloading using *args

class E:
    def add(self, *args):
        print(sum(args))

e = E()
e.add(1,2,3,4,5)



#3. operator overloading

class F:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, amount):
        return self.balance + amount

    def __sub__(self, amount):
        return self.balance - amount



f = F(200)

print(f-2)
