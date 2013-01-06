# Type Conversion
"""The process of converting the value of one data type (integer, string, float, etc.) 
to another data type is called type conversion. 
Python has two types of type conversion."""

# Implicit Type Conversion
"""In Implicit type conversion, Python automatically converts one data type to 
another data type. This process doesn't need any user involvement."""

"""Let's see an example where Python promotes the conversion of the lower 
data type (integer) to the higher data type (float) to avoid data loss."""

# Converting integer to float
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))


# Explicit Type Conversion
"""In Explicit Type Conversion, users convert the data type of 
an object to required data type. We use the predefined functions like 
int(), float(), str(), etc to perform explicit type conversion."""

"""This type of conversion is also called typecasting because 
the user casts (changes) the data type of the objects."""

# Addition of string and integer using explicit conversion

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

# Key Points to Remember
"""Type Conversion is the conversion of object from one data type to another data type."""

"""Implicit Type Conversion is automatically performed by the Python interpreter."""

"""Python avoids the loss of data in Implicit Type Conversion."""

"""Explicit Type Conversion is also called Type Casting, the data types of objects 
are converted using predefined functions by the user."""

"""In Type Casting, loss of data may occur as we enforce the object to a specific data type."""
