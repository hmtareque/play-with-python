"""Literal is a raw data given in a variable or constant. 
In Python, there are various types of literals they are as follows:"""

"""Numeric Literals are immutable (unchangeable). 
Numeric literals can belong to 3 different numerical types: 
Integer, Float, and Complex."""

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)


"""A string literal is a sequence of characters surrounded by quotes. We can use both single, 
double, or triple quotes for a string. And, a character literal is a single character 
surrounded by single or double quotes."""

# String literals in Python
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

