"""The break statement terminates the loop containing it. 
Control of the program flows to the statement immediately after the body of the loop."""

# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

"""The continue statement is used to skip the rest of the code inside a 
loop for the current iteration only. Loop does not terminate but continues on 
with the next iteration."""

# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")