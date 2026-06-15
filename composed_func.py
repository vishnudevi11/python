# A composed func. is when the output of one func. becomes the input of another - like f(g(x))

def add(x):
    return x + 1

def multi(x):
    return x * 2

def compose(x):
    return add(multi(x))

print(compose(20))