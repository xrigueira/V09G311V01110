"""
Diseñe un programa en Python en el que, utilizando funciones, para cada parte haga lo siguiente:

En un proceso que deberá ser repetitivo, el usuario podrá crear dos matrices bidimensionales con un máximo
de 5 filas y 5 columnas, por tanto de orden no superior a 25 y que no tiene que ser, necesariamente, cuadrada.
(es decir, puede ser de 5x5, 4x5, 3x2 o cualquier combinación que no sobrepase el 5x5).

Las matrices se cargarán con valores que deben ser dados por el usuairo y que deben estar entr 1 y 10 (ambos incluidos)
y que deben ser de tipo real.

La matriz se cargará en la opción 0 del menú que será:

    0. Definir el orden de la matriz y cargarla.
    1. Sumar las diagonales principales.
    2. Sumas la dos matrices y dar el resultado.
    3. Visualizarlas en forma de lista.
    4. Salir.
"""

def cargar_matriz():
    print("Cargar matriz")

    filas = -1
    while filas < 1 or filas > 5:
        filas = int(input("Ingrese el número de filas (máximo 5): "))
        if filas < 1 or filas > 5:
            print("El número de filas debe ser entre 1 y 5")

    columnas = -1
    while columnas < 1 or columnas > 5:
        columnas = int(input("Ingrese el número de columnas (máximo 5): "))
        if columnas < 1 or columnas > 5:
            print("El número de columnas debe ser entre 1 y 5")
    
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor de la posición {i+1},{j+1}: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_diagonales(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def sumar_matrices(matriz1, matriz2):
    matriz_suma = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        matriz_suma.append(fila)
    return matriz_suma

def visualizar_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    matriz1 = []
    matriz2 = []
    opcion = 0
    while opcion != 4:
        print("Menú")
        print("0. Definir el orden de la matriz y cargarla.")
        print("1. Sumar las diagonales principales.")
        print("2. Sumar las dos matrices y dar el resultado.")
        print("3. Visualizarlas en forma de lista.")
        print("4. Salir.")
        opcion = int(input("Ingrese la opción: "))
        if opcion == 0:
            matriz1 = cargar_matriz()
            matriz2 = cargar_matriz()
        elif opcion == 1:
            suma1 = sumar_diagonales(matriz1)
            suma2 = sumar_diagonales(matriz2)
            print(f"La suma de la diagonal principal de la matriz 1 es: {suma1}")
            print(f"La suma de la diagonal principal de la matriz 2 es: {suma2}")
        elif opcion == 2:
            matriz_suma = sumar_matrices(matriz1, matriz2)
            print("La matriz suma es:")
            visualizar_matriz(matriz_suma)
        elif opcion == 3:
            print("Matriz 1:")
            visualizar_matriz(matriz1)
            print("Matriz 2:")
            visualizar_matriz(matriz2)
        elif opcion == 4:
            print("Saliendo...")
        else:
            print("Opción inválida")


main()