#python program to find the factorial of a number
N = int(input("Enter the number: "))
factorial = 1
for i in range(1, N + 1):
    factorial = factorial * i
print(f"The factorial of {N} is {factorial}")
