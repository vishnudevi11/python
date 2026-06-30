import logging

# basic configuration

logging.basicConfig(
    level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
filename='app.log',
filemode='w')


def divide(a,b):
    print(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        # print(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.log("Error:Tried to divide by zero!")
        return None

divide(2,3)
divide(2,0)