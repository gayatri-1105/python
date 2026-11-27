employee = {
    101: {
        "name": "Rahul",
        "department": "IT",
        "salary": 30000
    },
    102: {
        "name": "Priya",
        "department": "HR",
        "salary": 40000
    },
    103: {
        "name": "Amit",
        "department": "Sales",
        "salary": 25000
    }
}

print("Employee Details:", employee)

employee[104] = {
    "name": "Sneha",
    "department": "IT",
    "salary": 50000
}

print("After Adding:", employee)

employee[101]["salary"] = 35000
print("After Updating:", employee)

del employee[103]
print("After Deleting:", employee)

print("Keys:", employee.keys())
print("Values:", employee.values())
print("Items:", employee.items())

search_id = int(input("Enter Employee ID: "))

if search_id in employee:
    print("Employee Found:", employee[search_id])
else:
    print("Employee Not Found")

high_salary = {
    emp_id: details
    for emp_id, details in employee.items()
    if details["salary"] > 30000
}

print("Employees earning above 30000:", high_salary)
