x = 100

def display():
    global x
    y = 50
    print("Global variable:", x)
    print("Local variable:", y)

def change():
    global x
    x = 200

display()
change()

print("Updated global variable:", x)

square = lambda n: n * n
cube = lambda n: n * n * n
maximum = lambda a, b: a if a > b else b
addition = lambda a, b: a + b

print("Square:", square(5))
print("Cube:", cube(3))
print("Maximum:", maximum(10, 20))
print("Addition:", addition(10, 20))
