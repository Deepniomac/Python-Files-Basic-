#python program to print set of odd numbers b/w 1 to N
n = int(input("Enter the N value : "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i,end=" ")
    i += 1

else : print("Good bye !")