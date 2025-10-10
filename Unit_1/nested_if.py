
#python program to implement nested-if statement
age = int(input("Enter age : "))
member = True
if age >= 18:
    if member:
        print(f"You are {age} years old and ticket price is 20/-")
    else:
        print(f"You are {age} years old and ticket price is 10/-")
else:
    if member:
        print(f"You are {age} years old and ticket price is 8/-")
    else :
        print(f"You are {age} years old and ticket price is 5/-")
