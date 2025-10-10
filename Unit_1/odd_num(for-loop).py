#python program to print odd numbers b/w 1 to N using for loop
N = int(input("Enter the N Value : "))
print("Odd numbers b/w 1 to N are : ")
print("----------------------------------")
for i in range(1,N+1,2):
    print(i,end=" ")
