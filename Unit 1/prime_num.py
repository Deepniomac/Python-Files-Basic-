#python program to check whether the given number is prime or not
n = int(input("Enter the number for prime number: "))
flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
if flag == True:
    print(f"The number {n} is prime")
else :
    print(f"The number {n} is not prime")