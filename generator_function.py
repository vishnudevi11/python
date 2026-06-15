# generator function is a special type of func. that uses the yeild keyword to return values one by one,instead of returning everything at once

# instead of return,we will use yield

# def get_numbers(n):
#     return [i for i in range(n)]
#
# print(get_numbers(5))

def get_numbers1(n):
    for i in range(n):
        yield i

for number in get_numbers1(5):
    print(number)
