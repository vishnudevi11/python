#  __init__ -> constructor
# constructor -> when object created and passing values
# self -> first argument,because s1 is a first argument


# class trip:
#
#     def __init__(self,fname,age):
#         self.name=fname
#         self.age=age
#
#     def display(self):
#         print(f"{self.name} is {self.age} years old")
#
# s1=trip("john",1)
# s1.display()


class Mathtool:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
m1=Mathtool( )
print(m1.add(3,4))