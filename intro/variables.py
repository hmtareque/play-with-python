"""A variable is a named location used to store data in the memory. 
It is helpful to think of variables as a container that holds data that 
can be changed later in the program."""

# For example

number = 10

# Here, we have created a variable named number. We have assigned the value 10 to the variable.

# You can think of variables as a bag to store books in it and that book can be replaced at any time.

number = 10
number = 1.1

# Initially, the value of number was 10. Later, it was changed to 1.1.

"""In Python, we don't actually assign values to the variables. 
Instead, Python gives the reference of the object(value) to the variable."""

#Assigning values to Variables in Python
"""As you can see from the above example, you can use the assignment operator = to assign 
a value to a variable."""

#Declaring and assigning value to a variable
website = "apple.com"
print(website)

"""In the above program, we assigned a value apple.com to the variable website. 
Then, we printed out the value assigned to website i.e. apple.com"""

"""Python is a type-inferred language, so you don't have to explicitly define the variable type. 
It automatically knows that apple.com is a string and 
declares the website variable as a string.""" 

# Assigning multiple values to multiple variables
a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)

# If we want to assign the same value to multiple variables at once, we can do this as:

x = y = z = "same"

print (x)
print (y)
print (z)