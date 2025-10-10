#python program to calculate GCD of two numbers
m,n = [int(x) for x in input("Enter two numbers: ").split()]
a,b = m,n
if n > m:
    m,n = n,m
while n != 0:
    m,n = n,m % n
print(f"The GCD of {a} and {b} is {m}")