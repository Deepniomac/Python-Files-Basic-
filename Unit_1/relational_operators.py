#program to implement the relational operations
a = int(input("enter a value : "))
b = int(input("Enter b value : "))
if a > b :
    print("a is greater ")
elif a < b :
    print("b is greater ")
elif a == b :
    print("Both have same values ")
elif a >= b :
    print("a is greater or equal to b")
elif a <= b :
    print("a is less than or equal to b")
elif a != b :
    print("a is not equal to b")
else :
    print("Invalid values")
