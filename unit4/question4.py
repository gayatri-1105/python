#1 Math Library
import math

n = int(input("Enter a number: "))

print("Square Root:", math.sqrt(n))
print("Factorial:", math.factorial(n))
print("Power:", math.pow(n, 2))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))

#2 Random Library
import random

numbers = [10, 20, 30, 40, 50]

print("Random Integer:", random.randint(1, 100))
print("Random Element:", random.choice(numbers))

random.shuffle(numbers)

print("Shuffled List:", numbers)

#3 DateTime Library
import datetime

today = datetime.datetime.now()

print("Current Date and Time:", today)
print("Day:", today.day)
print("Month:", today.month)
print("Year:", today.year)

date1 = datetime.date(2026, 1, 1)
date2 = datetime.date(2026, 12, 31)

difference = date2 - date1

print("Difference Between Dates:", difference.days, "days")

