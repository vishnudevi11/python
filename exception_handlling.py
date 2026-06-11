# error -> indention and syntx
# exception -> code is correct,mathematical error (runtime error are exceptional error)

# print("Step 1: Start")
# a=10
# b=0
# result=a/b # here 10 can't divide by 0,its mathematical error
# print("Step 2: Result is",result)

# try -> throw -> except(catch) -> finally
# Example: banking(if any crash is happening,directly it will logout)
# zomato

# if i doesn't know the exception,we can write exception
print("Welcome to Zomato!")
try:
    numbers_of_items =int(input("How many items do you have?"))
    total_price=200*numbers_of_items
    average_price=total_price/numbers_of_items
    print("The average price is ",average_price)
except Exception:
    print("You cannot divide by zero")
finally: #always execute block
    print("logout")

print("Next code block")

# we can't handle exception in if-else block