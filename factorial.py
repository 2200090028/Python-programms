#write a python program to find factorial  of given number
n = int(input("Enter number"))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")
