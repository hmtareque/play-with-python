"""In Python, a function is a group of related statements that performs a specific task."""

"""A function definition that consists of the following components."""

"""Keyword def that marks the start of the function header."""

"""A function name to uniquely identify the function. Function 
naming follows the same rules of writing identifiers in Python."""

"""Parameters (arguments) through which we pass values to a function. They are optional."""

"""A colon (:) to mark the end of the function header."""

"""Optional documentation string (docstring) to describe what the function does."""

"""One or more valid python statements that make up the function body. 
Statements must have the same indentation level (usually 4 spaces)."""

"""An optional return statement to return a value from the function."""

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet("Hasan")

# Docstrings 

"""The first string after the function header is called 
the docstring and is short for documentation string. 
It is briefly used to explain what a function does."""

print(greet.__doc__)

# Example of return
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))