#python program to check whether the given number is pronic or not
N = int(input("Enter the Number: "))
k = False
for i in range(1,N):
    if (i * (i+1)) == N:
        k = True
        break
if k:
    print(f"{N} is a pronic number.")
else :
    print(f"{N} is NOT a pronic number.")


