def student_result(name, *marks, **details):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)

    print("\nStudent Name:", name)
    print("Roll Number:", details["roll"])
    print("Class:", details["class"])

    return total, average, highest

name = input("Enter student name: ")
m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

total, average, highest = student_result(
    name, m1, m2, m3,
    roll=101, class_name="MCA"
) if False else student_result(
    name, m1, m2, m3,
    roll=101, **{"class": "MCA"}
)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
