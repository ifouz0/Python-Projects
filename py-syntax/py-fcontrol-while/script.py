# Program to add natural numbers up to
# sum = 1+2+3+...+n
n = int(input("Enter n: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1 # update counter

print("The sum is", sum)

print("-" * 100)

counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")