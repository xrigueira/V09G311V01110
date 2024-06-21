"""
Sea un fichero (datos.txt) que contiene información sobre una serie de productos almacenados:

Oro, 127, 136.15
Uranio, 0, 25.14
Carbón, 1450, 2.13
…
Diseñar un programa que solicite al usuario el nombre de un fichero hasta que el nombre indicado se corresponda con un fichero existente.
Una vez establecido el fichero con el que se va a trabajar, se presentará al usuario un menú que le permitirá elegir entre:
a)	Introducir nuevo producto
b)	Visualizar el contenido del almacén incluyendo también el cálculo del valor almacenado
c)	Obtener y visualizar un listado de aquellos productos en los que no hay existencias en el almacén
d)	Salir del programa


Ejemplo de visualización de contenido:
            MINERAL               CANTIDAD             PRECIO                VALOR ALMACENADO
            Oro                   127                  136.15                17291.05
            Uranio                0                    25.14                 0.00
            Carbón                1450                 2.13                  3088.50

"""

import os

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

# Definir función para crear un fichero
def obtener_nombre_fichero():

    fichero_correcto = False
    while not fichero_correcto:

        # Preguntar al usuario cuál es el fichero sobre el que se va a ejecutar el programa
        ruta = os.getcwd() + '\\Finals\\June'
        print('La ruta actual es:', ruta)

        nombre_fichero = input('Introduzca el nombre del fichero: ')
        ruta_fichero = ruta + '\\' + nombre_fichero + '.txt'
        print('La ruta del fichero es:', ruta_fichero)

        # Notificar al usuario si ya existe un fichero con el nombre indicado
        if os.path.exists(ruta_fichero):
            print('Nombre ya existente. Se procederá a trabajar con dicho fichero.')
            fichero_correcto = True

        else:
            print('Nombre no existente. Introduzca un nombre válido.')
    
    return ruta_fichero

# Definir función para la carga de datos
def carga_datos(ruta_fichero):
    
    # opcion_carga = input("Queres meter datos no ficheiro (S/n)?: ")
    opcion_carga = "S"
    
    datos = text2matrix(ruta_fichero)

    while "N" != opcion_carga.upper():
        nombre_mineral = str(input("Dame el nombre del mineral: "))
        codigo_mineral = str(input("Dame el peso atómico: ")) 
        precio = str(input("Dame el precio/kg: "))
        datos.append([nombre_mineral, codigo_mineral, precio])
        
        opcion_carga = input("¿Quieres meter más datos (n=no)? ")

    matrix2text(datos, ruta_fichero)

# Definir función para visualizar el contenido del almacén
def visualizar_almacen(ruta_fichero):
    
    datos = text2matrix(ruta_fichero)
    
    print("MINERAL               CANTIDAD             PRECIO                VALOR ALMACENADO")
    for row in datos:
        cantidad = int(row[1])
        precio = float(row[2])
        valor_almacenado = cantidad * precio
        print("{:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], valor_almacenado))

# Definir función para obtener y visualizar un listado de aquellos productos en los que no hay existencias en el almacén
def productos_sin_existencias(ruta_fichero):
    
    datos = text2matrix(ruta_fichero)
    
    print("MINERAL               CANTIDAD             PRECIO                VALOR ALMACENADO")
    for row in datos:
        cantidad = int(row[1])
        precio = float(row[2])
        valor_almacenado = cantidad * precio
        if cantidad == 0:
            print("{:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], valor_almacenado))

# Obtener el nombre del fichero
ruta_fichero = obtener_nombre_fichero()

# Menú de opciones
opcion = 0
while opcion != 5:
    print('1. Introducir nuevo producto')
    print('2. Visualizar el contenido del almacén')
    print('3. Obtener y visualizar un listado de aquellos productos en los que no hay existencias en el almacén')
    print('4. Salir del programa')
    opcion = int(input('Introduzca la opción deseada: '))

    if opcion == 1:
        carga_datos(ruta_fichero)
    elif opcion == 2:
        visualizar_almacen(ruta_fichero)
    elif opcion == 3:
        productos_sin_existencias(ruta_fichero)
    elif opcion == 4:
        break
    else:
        print('Opción no válida')