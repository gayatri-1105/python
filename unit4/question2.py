# Write student details
f = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
course = input("Enter course: ")

f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Course: " + course + "\n")

f.close()

# Read complete file
f = open("student.txt", "r")

print("\nFile Contents:")
print(f.read())

f.close()

# Append additional details
f = open("student.txt", "a")

f.write("\nAdditional Student: Rahul\n")
f.write("Roll Number: 102\n")

f.close()

# Read file line by line
f = open("student.txt", "r")

print("\nReading Line by Line:")

for line in f:
    print(line.strip())

f.close()

# Display all lines
f = open("student.txt", "r")

print("\nAll Lines:")
print(f.readlines())

f.close()
