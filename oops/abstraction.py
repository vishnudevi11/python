from abc import ABC, abstractmethod

# this abstract method
class FeaturePlan(ABC):
    @abstractmethod
    def login(self):
        print("hello")
    @abstractmethod
    def logout(self):
        pass

    def checkout(self):
        pass
class Webapp(FeaturePlan):
    def login(self):
        print("login to webapp✅")
    def logout(self):
        print("logout to webapp✅")

a=Webapp()
a.login()


a.logout()