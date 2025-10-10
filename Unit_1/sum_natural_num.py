#python program to add natural  numbers
N = int(input("Enter the N value: "))
sum = 0
for i in range(1, N+1):
    sum += i
print(f"The sum of {N} natural numbers is {sum}")
