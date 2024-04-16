import random

matrix = []

# Ask the user for the number of rows and columns
try:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
except ValueError:
    print('Please enter an integer')

# Fill up the matrix with empty elements
for i in range(rows):
    matrix.append([0]*columns)

# Fill up each position with a random integer
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = random.randint(0, 100)

# Print the matrix
print(matrix)