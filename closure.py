def outer(msg):
    def inner():
        return("Message is : "+msg)
    return inner
say_hi=outer("Hallo,ich bin vishnudevi")
print(say_hi())