#program to find the gratest among two numbers
a,b = [int(x) for x in input("enter a, b values : ").split()]
if a > b :
    print(f"{a} is grater than {b}")
else :
    print(f"{a} is not greater than {b}")
