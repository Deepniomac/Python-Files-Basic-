#program to find the greatest among three numbers
a,b,c = [int(i) for i in input("Enter three values : ").split()]
if a > b and a > c :
    print(f"{a} is greater than {b} and {c} ")
elif b > a and b > c :
    print(f"{b} is greater than {a} and {c} ")
else :
    print(f"{c} is greater than {a} and {b} ")

