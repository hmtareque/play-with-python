"""
    Number data types store numeric values. 
    Number objects are created when you assign a value to them. 
"""

num = 1076
print(num)

"""
    Python supports four different numerical types: 
    - int (signed integers) They are often called just integers or ints. 
        They are positive or negative whole numbers with no decimal point. 
        Integers in Python 3 are of unlimited size. 
        Python 2 has two integer types - int and long. 
        There is no 'long integer' in Python 3 anymore.
    - float (floating point real values) Also called floats, they represent real numbers 
        and are written with a decimal point dividing the integer and the fractional parts. 
        Floats may also be in scientific notation, with E or e indicating the power of 10
    - complex (complex numbers) are of the form a + bJ, where a and b are floats and J (or j) 
        represents the square root of -1 (which is an imaginary number). 
        The real part of the number is a, and the imaginary part is b. 
        Complex numbers are not used much in Python programming.
"""

num_int = 8 #int 
num_float = 90.75 #float 
num_complex = 3.2j #complex 

# to show datatype 
print(type(num_int))
print(type(num_float))
print(type(num_complex))

# Number conversion 

con_int_to_float = float(num_int)
print(type(con_int_to_float))

""" Python converts numbers internally in an expression containing mixed types to 
    a common type for evaluation. Sometimes, you need to coerce a number explicitly 
    from one type to another to satisfy the requirements of an operator or function parameter.

    - Type int(x) to convert x to a plain integer.
    - Type float(x) to convert x to a floating-point number.
    - Type complex(x) to convert x to a complex number with real part x and imaginary part zero.
    - Type complex(x, y) to convert x and y to a complex number with real part x and 
        imaginary part y. x and y are numeric expressions
"""





