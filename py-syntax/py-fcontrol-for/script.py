
for val in range(0, 100):
    print(val)
else:
    print("For finished!!!")

print("-" * 100)

for val in range(0, 100, 5):
    print(val)
else:
    print("For finished!!!")

print("-" * 100)

# Program to show the use of break statement inside loops
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

print("-" * 100)

# Program to show the use of continue statement inside loops
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
