#Python Numbers
"""Integers, floating point numbers and complex numbers fall under Python numbers category. 
They are defined as int, float and complex classes in Python."""

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


# Python List
"""List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. 
All the items in a list do not need to be of the same type."""

"""Declaring a list is pretty straight forward. 
Items separated by commas are enclosed within brackets [ ]."""

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

# Python Tuple
"""Tuple is an ordered sequence of items same as a list. 
The only difference is that tuples are immutable. Tuples once created cannot be modified."""

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])