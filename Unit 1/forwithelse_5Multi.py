#python program to print multiples of 5 using 'for' with 'else' statements
N = int(input("Enter the N value : "))
print(f"Multiples of 5 below {N} are :")
print("---------------------------------------")
for i in range(5,N+1,5):
    print(i,end=" ")
