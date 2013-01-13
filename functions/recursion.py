"""Recursion is the process of defining something in terms of itself."""

"""A physical world example would be to place two parallel mirrors facing each other. 
Any object in between them would be reflected recursively."""

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

# Advantages of Recursion
"""Recursive functions make the code look clean and elegant."""
"""A complex task can be broken down into simpler sub-problems using recursion."""
"""Sequence generation is easier with recursion than using some nested iteration."""

# Disadvantages of Recursion
"""Sometimes the logic behind recursion is hard to follow through."""
"""Recursive calls are expensive (inefficient) as they take up a lot of memory and time."""
"""Recursive functions are hard to debug."""