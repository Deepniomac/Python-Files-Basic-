"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
rows = int(input("Enter the number of rows : "))
for row in range(1, rows + 1):
    for col in range(1, row + 1):
        print(row, end=" ")
    print()