# giving access to variables
# public,private,protected

class Parent:
    def __init__(self):
        self.public_var="I'm Public"
        self._protected_var="I'm Protected"
        self.__private_var = "I'm Private"

    def access_from_same_class(self):
        print("Inside parent class")
        print("public:",self.public_var)
        print("protected:",self._protected_var)
        print("private:",self.__private_var)

class Child(Parent):
    def access_from_subclass(self):
        print("Inside child class")
        print("public:",self.public_var)
        print("protected:",self._protected_var)
        # private cannot access in the subclass,it can be access in the same class
        try:
            print("private:",self._Parent__private_var)  #we can access using Parent class
        except:
            print(f"{AttributeError}")

p=Parent()
c=Child()
p.access_from_same_class()
c.access_from_subclass()