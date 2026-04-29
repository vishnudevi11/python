# Block of reuseable code

# def great():
#     print("Welcome to function")
#
# great()

# function with argu
# def great(name):
#     print(f"Hello {name}" )
#
# great("vishnu")

# def add(a,b):
#     print(a+b)
# add(3,5)

# return ,returns some other function or classes
# print is just to see
# def add(a,b):
#     return a+b
# result = add(3,4)
# print(result)

# def add(a,b):
#     return (a+b)


# *args (accept multiple arguments)

# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     # 0+=1
#     # 1+=2
#     # 3+=2
#     # 5
#     return total
#
# print(add(1,2,2))

# **kwargs  key value pairs
def create_profile(**kwargs):
    print("User Profile")
    for key,value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="vishnu",age=33,job="Data engineer")