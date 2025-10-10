"""count = 5
k = 1
for i in range(0,6):
    for x in range(i,count + 1):
        print("*",end =" ")
    if k <= i :
        for y in range(i,count + 1):
            print()
    count -= 1
    print()
"""
str = "lendi"
size = 5
k = 0
for x in range(1,size+1):
    for i in range(size,x,-1):
        print(" ",end="")
    for j in range(1,2 * x):
        print(str[k], end="")
        k = k + 1

        if k == len(str):
            k = 0
    print()