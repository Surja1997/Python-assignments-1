matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [-34, 22, 4, 9], [32, 43, 76, 45]]
cols: int = len(matrix[0])
space = 0;
for i in range(len(matrix) - 1):
    for k in range(space):
        print(" ", end="")
    for j in range(i + 1, cols):
        print(matrix[i][j], end=" ")
    space += 2
    print()
print("-------------------------------------")
matrix.pop([0][0])
print(matrix)
