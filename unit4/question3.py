try:
    f = open("student.txt", "r")

    print("File Name:", f.name)
    print("File Mode:", f.mode)

    print("\nRead Method:")
    print(f.read())

    f.seek(0)

    print("\nReadline Method:")
    print(f.readline())

    f.seek(0)

    print("\nReadlines Method:")
    print(f.readlines())

    print("Current Position:", f.tell())

    f.seek(0)
    print("After Seek:", f.tell())

except FileNotFoundError:
    print("File does not exist")

except PermissionError:
    print("Permission denied")

else:
    print("File operations completed successfully")

finally:
    try:
        f.close()
        print("File closed")
    except NameError:
        print("File was not opened")
