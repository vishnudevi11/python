# A recursive func. is a func. that call itself in order to solve a smaller version of the same problem.

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(factorial(5))