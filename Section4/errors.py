# use the try/except framework to help work with errors

# Get user input
a = int(input("Enter your numerator: "))
b = int(input("Enter your denominator: "))

# define function here
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero is meaningless"

# print result of the function call
print(divide(a,b))
print("End of program")
