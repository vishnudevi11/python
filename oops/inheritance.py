# code reusablity,it inherites child class from parent class
# if we want to over write,call house method in child class

# class dad: #parent
#     def house(self):
#         print("I am from dad class")
#
# class son(dad):  #child
#     def factory(self):
#         print("I am from test class")
#
#         # overwrite
#     def house(self):
#         print("I am from son class")


# class app1():
#     def v1(self):
#         print("Orders")
# class app_1(app1):
#     def v1(self):
#         print("refund")
#
# a=app_1()
# a.v1()


# multilevel inheritance
# class grandfather():
#     def car(self):
#         print("red car")
# class dad(grandfather):
#     def house(self):
#         print("Red")
# class son(dad):
#     def house(self):
#         print("house white")
#
# v=son()
# v.house()
# v.car()


# multiple inheritance
# class dad:
#     def house(self):
#         print("House is working")
#
# class mom:
#     def shop(self):
#         print("Shop is working")
#
# class daughter(dad,mom):
#     def factory(self):
#         print("Factory is working")
#
# d=daughter()
# d.house()
# d.factory()
# d.shop()




