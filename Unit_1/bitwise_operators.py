#program to implement the bitwise operations
a,b = [int(i) for i in input("Enter a,b values : ").split()]
print(f"Bitwise And : {a & b}")
print(f"Bitwise Or : {a ^ b}")
print(f"Bitwise exclusive Or : {a | b}")
print(f"Shift right : {a>>b}")
print(f"Shift left : {a<<b}")
print(f"Complement : {~a}")
