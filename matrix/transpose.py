def transpose(matrix):

    rows = len(matrix)
    columns = len(matrix[0])
    transpose_matrix = []

    # Crear matriz transpuesta vacia
    for i in range(columns):
        new_row = []
        for j in range(rows):
            new_row.append(0)
        transpose_matrix.append(new_row)

    # Completar matriz transpuesta
    for i in range(rows):
        for j in range(columns):
            transpose_matrix[j][i] = matrix[i][j]

    # Mostrar matriz transpuesta
    for i in range(len(transpose_matrix)):
        print(f"{transpose_matrix[i]}")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose(matriz)
