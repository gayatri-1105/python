import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
operator = sys.argv[3]

if operator == "+":
    result = a + b

elif operator == "-":
    result = a - b

elif operator == "*":
    result = a * b

elif operator == "/":
    if b == 0:
        result = "Cannot divide by zero"
    else:
        result = a / b

else:
    result = "Invalid operator"

print("Result:", result)
