#python program to print a math table using for loop
N = int(input("Enter the table number: "))
ran = int(input("Enter the range: "))
print(f"The multiples of {N} upto {ran} steps : ")
i = 1
for i in range(i<=N,ran+1) :
    print(f"{N} * {i} = {N * i} ")
