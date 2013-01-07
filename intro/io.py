"""Python provides numerous built-in functions that are readily available to us at the Python prompt."""

"""In the second print() statement, we can notice that space was added between the string and 
the value of variable a. This is by default, but we can change it."""

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

"""Here, objects is the value(s) to be printed."""

"""The sep separator is used between the values. It defaults into a space character."""

"""After all values are printed, end is printed. It defaults into a new line."""

"""The file is the object where the values are printed and its default value 
is sys.stdout (screen). Here is an example to illustrate this."""

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

"""Sometimes we would like to format our output to make it look attractive. 
This can be done by using the str.format() method. This method is visible to any string object."""

x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))

"""Here, the curly braces {} are used as placeholders. 
We can specify the order in which they are printed by using numbers (tuple index)."""

print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))

"""We can also format strings like the old sprintf() style used in C programming language. 
We use the % operator to accomplish this."""

x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)

# Python Input
"""Up until now, our programs were static. 
The value of variables was defined or hard coded into the source code."""

"""To allow flexibility, we might want to take the input from the user. 
In Python, we have the input() function to allow this."""

# The syntax for input() is:
num = input('Enter a number: ')

# Python Import
"""When our program grows bigger, it is a good idea to break it into different modules.
Definitions inside a module can be imported to another module or the interactive interpreter in Python. 
We use the import keyword to do this."""

# For example, we can import the math module by typing the following line:

# import math 
# print(math.pi)