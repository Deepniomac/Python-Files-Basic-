# Python Program to implement different arguments in function
def calculate(a,b):
    sum_ = a + b
    diff_ = a - b
    prod_ = a * b
    return (sum_, diff_, prod_)
[x, y, z] = calculate(100, 20)
print(f"The sum is : {x}")
print(f"The Difference is : {y}")
print(f"The Product is : {z}")