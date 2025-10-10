#python program to consider a person age and find their status
"""
age > 60 - senior citizen
age 25 to 59 - working citizen
age 16 to 24 - college students
age 4 to 15 - school kids
age 1 to 3 - play kids
else display - invalid
"""
age = int(input("Enter age: "))
if age >= 60 :
    print("Age is older than 60 i.e 'senior citizen'")
elif age >= 25 and age <= 59 :
    print("Age is older than 25 i.e 'working citizen'")
elif age >= 16 and age <= 24 :
    print("Age is older than 16 i.e 'college students'")
elif age >= 4 and age <= 15 :
    print("Age is older than 4 i.e 'school kids'")
elif age >= 1 and age <= 3 :
    print("Age is older than 1 i.e 'play kids'")
else :
    print("Invalid")