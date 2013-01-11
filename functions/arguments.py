"""In the user-defined function topic, we learned about defining a function 
and calling it. Otherwise, the function call will result in an error. """

def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")

# Function arguments can have default values in Python.

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")


# Python Keyword Arguments
"""When we call a function with some values, 
these values get assigned to the arguments according to their position."""

# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?", name = "Bruce") 

# 1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?") 