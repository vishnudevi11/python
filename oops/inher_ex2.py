from oops.inheritance import dad

class son(dad):
    def factory(self):
        print("White")
    def house(self):
        print("yellow")

s=son()
s.factory()
s.house()