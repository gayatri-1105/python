t = (101, 102, 103, 104, 105)

print("Tuple:", t)
print("Indexing:", t[0])
print("Slicing:", t[1:4])
print("Concatenation:", t + (106, 107))

set1 = {101, 102, 103, 104}
set2 = {103, 104, 105, 106}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

print("Subset:", {103, 104}.issubset(set1))
print("Superset:", set1.issuperset({101, 102}))

set1.add(110)
print("After Add:", set1)

set1.remove(110)
print("After Remove:", set1)

squares = {x * x for x in range(1, 11) if x % 2 == 0}

print("Squares of Even Numbers:", squares)
