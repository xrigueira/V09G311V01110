import time
import random

import numpy as np

# Define a function to create a matrix of n rows and m columns filled with random numbers between 1 and 99
def create_matrix(rows, columns):
    
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(random.randint(1, 100))
        matrix.append(row)
    
    return matrix

def create_matrix_faster(rows, columns):
    matrix = np.random.randint(1, 100, size=(rows, columns))
    return matrix.tolist()

# Define a function to multiplica two matrices of the same dimensions
def mat_sum(matrix1, matrix2):
    
    matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        matrix.append(row)

    return matrix


if __name__ == '__main__':

    fast = False

    times = []
    for _ in range(20):
    
        start = time.time()
        # Create two matrices
        rows = 2000
        columns = 2000
        if fast:
            matrix1 = create_matrix_faster(rows=rows, columns=columns)
            matrix2 = create_matrix_faster(rows=rows, columns=columns)
        else:
            matrix1 = create_matrix(rows=rows, columns=columns)
            matrix2 = create_matrix(rows=rows, columns=columns)
        end_create_matrix = time.time() - start
        # print('Matrix creation ran in', end_create_matrix, 'seconds')

        # Multiply both matrices
        result = mat_sum(matrix1=matrix1, matrix2=matrix2)
        end_multiply_matrix = time.time() - end_create_matrix - start
        # print('Matrix addition ran in', end_multiply_matrix, 'seconds')
        
        times.append((end_create_matrix, end_multiply_matrix))
    
    # Get the average time for matrix creation and multiplication
    print('Average time for matrix creation:', sum([x[0] for x in times])/len(times))
    print('Average time for matrix multiplication:', sum([x[1] for x in times])/len(times))

