"""In the user-defined function topic, we learned about defining a function 
and calling it. Otherwise, the function call will result in an error. """

def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")