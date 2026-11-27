n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Original List:", numbers)

pos = int(input("Enter position to insert: "))
value = int(input("Enter value: "))
numbers.insert(pos, value)

print("After Insert:", numbers)

remove_value = int(input("Enter value to remove: "))

if remove_value in numbers:
    numbers.remove(remove_value)

print("After Remove:", numbers)

print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

print("Concatenation:", numbers + [10, 20])
print("Repetition:", numbers * 2)

print("First Element:", numbers[0])
print("Membership:", 10 in numbers)

even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
squares = [x * x for x in numbers]

print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Squares:", squares)

numbers.extend([50, 60])
print("Extend:", numbers)

numbers.reverse()
print("Reverse:", numbers)

numbers.sort()
print("Sort:", numbers)

numbers.pop()
print("Pop:", numbers)
