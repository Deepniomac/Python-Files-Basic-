#python program to generate the fibnocci sequence
N = int(input("Enter the N value: "))
f1 = f2 = i = 1
print(f1,end = " ")
print(f2,end = " ")
while i <= N-1:
    f3 = f1 + f2
    print(f3,end = " ")
    f1 = f2
    f2 = f3
    i = i + 1