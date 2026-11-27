#1-arithmetic 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#2 - student/details
def student_details():
    print("Student Name: Gayu")
    print("Course: MCA")
    print("Roll Number: 101")

#3 - student/results.py
def student_result():
    marks = [80, 85, 90]
    print("Total:", sum(marks))
    print("Average:", sum(marks) / len(marks))

#4 - main.py
import arithmetic
from arithmetic import add, multiply
from student import student_details, student_result

print("Addition:", arithmetic.add(10, 20))
print("Subtraction:", arithmetic.subtract(20, 10))
print("Multiplication:", multiply(5, 4))
print("Division:", arithmetic.divide(20, 5))

print("Selected Addition:", add(5, 5))

student_details()
student_result()
