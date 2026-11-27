text = input("Enter a sentence: ")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Without spaces:", text.strip())

old = input("Enter word to replace: ")
new = input("Enter new word: ")

print("Replaced:", text.replace(old, new))

ch = input("Enter character to count: ")
print("Occurrences:", text.count(ch))

sub = input("Enter substring: ")

print("Starts with:", text.startswith(sub))
print("Ends with:", text.endswith(sub))

print("Concatenation:", text + " Python")
print("Repetition:", text * 2)
print("Membership:", "Python" in text)
