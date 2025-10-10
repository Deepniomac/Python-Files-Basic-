#python program to add two 3 X 3 matrix using nested loops
mat1 =[[1,2,3],[4,5,6],[7,8,9]]
mat2 =[[1,2,3],[4,5,6],[7,8,9]]

print("Mat1 = ")
for i in range(3):
    for j in range(3):
        print(mat1[i][j],end=" ")
    print()
print("\n------------------------------------------\n")
print("Mat2 = ")
for i in range(3):
    for j in range(3):
        print(mat2[i][j],end=" ")
    print()
print("\n------------------------------------------\n")
print("Result = ")
for i in range(3):
    for j in range(3):
        print(mat1[i][j]+mat2[i][j],end=" ")
    print()