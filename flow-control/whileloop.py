"""In the while loop, test expression is checked first. 
The body of the loop is entered only if the test_expression evaluates to True. 
After one iteration, the test expression is checked again. 
This process continues until the test_expression evaluates to False."""

# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
