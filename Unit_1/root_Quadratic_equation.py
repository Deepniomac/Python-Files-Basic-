#python program to find the sqaure root of a Quadratic Equation
from math import *
a,b,c = [int(x) for x in input("Enter the co.efficients of the Q.E : ").split()]
D = (b**2 - (4.0*a*c))
if D > 0 :
    print("Roots are real and distinct!")
    r1 = (-b + sqrt(D))/(2*a)
    r2 = (-b - sqrt(D))/(2*a)
    print("The roots are approximately ",r1," and ",r2)
elif D < 0 :
    print("Roots are Imaginary!")
else :
    print("Roots are real and Equal")
    r1 = r2 = (-b + sqrt(D))/(2*a)
    print(f"Root is : {r1}")
