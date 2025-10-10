#python program to check whether the given number is palindrome or not
n = int(input("Enter a number: "))
temp = n
rev = 0
while n != 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
if temp == rev:
    print(f"{temp} is a palindrome.")
else :
    print(f"{temp} is not a palindrome.")