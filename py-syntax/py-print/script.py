# print() function takes in any number of parameters and prints them out on one line of text. 
# The items are each converted to text form, separated by spaces, and there is a single '\n' at the end (the "newline" char). 
# When called with zero parameters, print() just prints the '\n' and nothing else.

print()
print("Hello world from Python with double quotes")
print("""Hello world from Python with triple double quotes""")
print('Hello world from Python with single quotes :)')
print('''Hello world from Python with triple single quotes :)''')

print("-" * 50)

print("My name's is Jordi")
print('My name\'s is Jordi')
print()

print("-" * 50)

print("S1", "S2", "S3", "S4",)
print('S1', 'S2', 'S3', 'S4')

print("S1", "S2", "S3", "S4", sep = "****")
print("S1", "S2", "S3", "S4", end = "\n---------------------------------------\n")

print("S1", "S2", "S3", "S4", end = "\n", sep = "****")
print("S1", "S2", "S3", "S4", sep = "****", end = "\n")

print("-" * 50)

print("You can write a new line character inside with \\n \n")
print("You can write \\ character")

print("-" * 50)

# Using raw strings
print(r"C:\Users\jordi")
print(R"C:\Users\jordia")

print("-" * 50)