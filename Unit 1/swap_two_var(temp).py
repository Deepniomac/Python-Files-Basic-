#program to swap any two variables using a temporary variable
a = int(input("Enter a value : "))
b = int(input("Enter b value : "))

print("Before entering a,b values : ")
print(f"a = {a}")
print(f"b = {b}")

#swapping using a temporary variable
t = a
a = b
b = t

print("after entering a,b values : ")
print(f"a = {a}")
print(f"b = {b}")
