# A callback func. is a func. that you pass as an argument to another func.,so that it can be called (executed) later,usually after some action is completed.

def on_button(callback):
    print("Button clicked") #once the print got executed
    callback()

def show_message():
    print("Hello Vishnu,Welcome!")

on_button(show_message)
