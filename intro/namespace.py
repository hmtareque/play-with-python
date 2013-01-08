"""Name (also called identifier) is simply a name given to objects. 
Everything in Python is an object. Name is a way to access the underlying object."""

# You may get different values for the id
a = 2
print('id(2) =', id(2))
print('id(a) =', id(a))

"""This is efficient as Python does not have to create a new duplicate object. 
This dynamic nature of name binding makes Python powerful; 
a name could refer to any type of object."""

a = 5
a = 'Hello World!'
a = [1,2,3]

"""All these are valid and a will refer to three different types of objects in different instances. 
Functions are objects too, so a name can refer to them as well."""

def printHello():
    print("Hello")

a = printHello
a()

# Namespace in Python
"""Now that we understand what names are, we can move on to the concept of namespaces."""
"""To simply put it, a namespace is a collection of names."""
"""In Python, you can imagine a namespace as a mapping of every 
name you have defined to corresponding objects."""


"""At any given moment, there are at least three nested scopes."""

# Scope of the current function which has local names
# Scope of the module which has global names
# Outermost scope which has built-in names

def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)




