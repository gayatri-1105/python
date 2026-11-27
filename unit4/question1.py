try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Division:", result)

    numbers = [10, 20, 30]
    index = int(input("Enter list index: "))

    print("List Element:", numbers[index])

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

except IndexError:
    print("Invalid list index")

else:
    print("No exception occurred")

finally:
    print("Program execution completed")

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Eligible")
except ValueError as e:
    print(e)
