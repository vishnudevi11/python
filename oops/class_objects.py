# class is a blueprint
class Student:
    # method
    def say_hello(self):
        print("Hello")
# s1
# caller(obj)
s1 = Student()
s1.say_hello() #s1.say_hello(s1)


# multiple objects

class Students:
    # constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"{self.name} is {self.age} years old")

s1=Students('John',25)
s2=Students('Vishnu',25)

s1.display()
s2.display()
