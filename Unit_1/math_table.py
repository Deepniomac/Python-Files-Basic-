#python program to print the mathematical table
tno = int(input("Enter the table number : "))
n = int(input("Enter the limit : "))
i = 1
while i <= n:
    r = i * tno
    print(f"{tno} * {i} = {r} ")
    i += 1
