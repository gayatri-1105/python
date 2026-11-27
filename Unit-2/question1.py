def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculate(a, b, operation="all"):
    print("Addition:", add(a=a, b=b))
    print("Subtraction:", subtract(a=a, b=b))
    print("Multiplication:", multiply(a=a, b=b))
    print("Division:", divide(a=a, b=b))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

calculate(x, y)
