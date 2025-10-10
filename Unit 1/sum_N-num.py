#python program to sum up all the N natural numbers i.e 1+2+3+4+5+......N
N = int(input("Enter the N value: "))
ad = 0
for i in range(1,N+1):
    ad = ad + i
print(f"The sum of first {N} natural numbers is {ad}.")