# Una función que, partiendo de una matriz y un nº de columna, devuelva la suma de los elementos de esa columna.
def sum_column(matrix, column):
    total = 0
    for row in matrix:
        total += float(row[column])
    
    return total

# Una función que, partiendo de una matriz y un nº de columna, devuelva el mínimo de los elementos de esa columna.
def min_column(matrix, column):
    minimum = float(matrix[0][column])
    for row in matrix:
        if float(row[column]) < minimum:
            minimum = float(row[column])
    
    return minimum

# Una función que, partiendo de una matriz, un nº de columna y un valor numérico, devuelva, en una lista, los elementos que, almacenados en la columna indicada de la matriz, superan el valor numérico indicado.
def elements_above(matrix, column, value):
    elements = []
    for row in matrix:
        if float(row[column]) > value:
            elements.append((row[0]))
    
    return elements

# Una función que transforma un fichero de texto en una matriz.
def text2matrix(filepath):
    matrix = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            matrix.append(list(line))
    
    return matrix

# Una función que transforma una matriz en un fichero de texto.
def matrix2text(matrix, filepath):
    with open(filepath, 'w') as file:
        for row in matrix:
            file.write(','.join(row) + '\n')