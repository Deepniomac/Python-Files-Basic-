#python program to find the distance b/w two points in 2D co.ordinate
from math import sqrt
x1,y1 = [int(x) for x in input("Enter the P co.ordinates : ").split()]
x2,y2 = [int(x) for x in input("Enter the Q co.ordinates : ").split()]
dist = (x2-x1)**2 + (y2-y1)**2
print(f"Distance b/w P and Q is : {sqrt(dist):.2f}")
