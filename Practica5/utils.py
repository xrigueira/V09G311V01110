# Una función que, partiendo de una matriz y un nº de columna, devuelva la suma de los elementos de esa columna.
def sum_column(matrix, column):
    total = 0
    for row in matrix:
        total += row[column]
    
    return total

# Una función que, partiendo de una matriz y un nº de columna, devuelva el mínimo de los elementos de esa columna.
def min_column(matrix, column):
    minimum = matrix[0][column]
    for row in matrix:
        if row[column] < minimum:
            minimum = row[column]
    
    return minimum

# Una función que, partiendo de una matriz, un nº de columna y un valor numérico, devuelva, en una lista, los elementos que, almacenados en la columna indicada de la matriz, superan el valor numérico indicado.
def elements_above(matrix, column, value):
    elements = []
    for row in matrix:
        if row[column] > value:
            elements.append(row)
    
    return elements

