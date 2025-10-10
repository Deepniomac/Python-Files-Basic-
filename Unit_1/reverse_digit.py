#python program to print reverse of a digit
n = int(input("Enter a number: "))
temp = n
rev = 0
while n != 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
print(f"The reverse digit of {temp} is {rev}")