total=0 #global

def add(amount):
    global total
    total += amount
    print("i'm from add()",total)

def test():
    print(total)

add(2)
test()