#program to swap any two variables without using a temporary variable
a = int(input("Enter a value : "))
b = int(input("Enter b value : "))

print("Before entering a,b values : ")
print(f"a = {a}")
print(f"b = {b}")

#swapping without using a temporary variable
a,b = b,a

print("after entering a,b values : ")
print(f"a = {a}")
print(f"b = {b}")
