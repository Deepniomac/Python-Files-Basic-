#python program to print all prime numbers b/w 1 to N
N = int(input("Enter the N value : "))
print(f"Prime numbers b/w 1 to {N} are :- ")
print("-------------------------------------------")
for i in range(2, N+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag == True:
        print(i, end=" ")