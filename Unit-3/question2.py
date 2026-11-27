name = input("Enter full name: ")
email = input("Enter email: ")
mobile = input("Enter mobile number: ")

words = name.split()

first = words[0]
last = words[-1]

print("First Name:", first)
print("Last Name:", last)
print("Reversed Name:", name[::-1])

email_parts = email.split("@")

print("Username:", email_parts[0])
print("Domain:", email_parts[1])

print("Last Four Digits:", mobile[-4:])

print("\nStudent Information")
print(f"Name: {name}")
print("Email: {}".format(email))
print("Mobile: %s" % mobile)

print("First Character:", name[0])
print("Last Character:", name[-1])
