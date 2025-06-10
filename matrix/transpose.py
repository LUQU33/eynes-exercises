def transpose(matrix):

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            print(f"{matrix[i][j]}")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose(matriz)
