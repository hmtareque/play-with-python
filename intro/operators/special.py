# Special operators
"""Python language offers some special types of operators like the identity 
operator or the membership operator."""

# Identity operators
"""is and is not are the identity operators in Python."""

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

# Membership operators
"""in and not in are the membership operators in Python. 
They are used to test whether a value or variable is found in a sequence 
(string, list, tuple, set and dictionary)."""

# Membership operators in Python
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y) 



