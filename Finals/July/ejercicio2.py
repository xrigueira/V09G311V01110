"""
Diseñar un programa que, en primer lugar, pregunte al usuario el nombre del fichero con el que va a trabajar. A continuación, se presentará al usuario un menú como el que se muestra a continuación:
    
    a) Cargar fichero
    b) Visualizar contenido del fichero
    c) Visualizar promedio de edad y de estatura
    d) Salir del programa

En la primera de las opciones (a), si el fichero ya existe, se preguntará al usuario si desea añadir más datos al fichero o desea reemplazarlo antes de proceder a su apertura.

Para resolver este ejercicio se utilizarán las funciones del módulo creado en el ejercicio anterior.

Además, se definirán las siguientes funciones:
    * Una función que sirva para visualizar el menú y que devuelva la opción elegida por el usuario.
    * Una función que, dada una matriz y un nombre de fichero, vuelque la información de la matriz en el fichero. (Esta función se utilizará en la opción a) del menú)
    * Una función que, dado un fichero, vuelque su contenido en una matriz y devuelva esta última. (Esta función se utilizará en las opciones b) y c) del menú)

Ensamblar todas las llamadas a las funciones en el programa principal para que resulte operativo y eficiente.
"""

import os
from modulo_ejercicio1 import cargar_matriz, media_columna

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

# Definir función para crear el fichero en caso de que no exista
def crear_fichero():

    # Preguntar al usuario cuál es el fichero sobre el que se va a ejecutar el programa
    ruta = os.getcwd() + '\\Finals\\July'
    print('La ruta actual es:', ruta)

    nombre_fichero = input('Introduzca el nombre del fichero: ')
    ruta_fichero = ruta + '\\' + nombre_fichero + '.txt'
    print('La ruta del fichero es:', ruta_fichero)

    # Notificar al usuario si ya existe un fichero con el nombre indicado
    if os.path.exists(ruta_fichero):
        print('Ya existe un fichero con el nombre indicado')

        # En caso de que exista un fichero con el nombre indicado, imprimir la información que contiene el fichero
        with open(ruta_fichero, 'r') as fichero:
            for line in fichero:
                print(line)
    else:
        fichero = open(ruta_fichero, 'w')
        fichero.close()
    
    return ruta_fichero

# Definir función para la carga de datos
def carga_datos(ruta_fichero):
    
    # opcion_carga = input("Queres meter datos no ficheiro (S/n)?: ")
    opcion_carga = "S"
    
    datos = text2matrix(ruta_fichero)

    while "N" != opcion_carga.upper():
        for i in range(5):
            fila = []
            nombre = input("Ingrese el nombre de la persona: ")
            edad = int(input("Ingrese la edad de la persona: "))
            estatura = float(input("Ingrese la estatura de la persona: "))
            fila.append(nombre)
            fila.append(edad)
            fila.append(estatura)
            datos.append(fila)
        
        opcion_carga = input("¿Quieres meter más datos (n=no)? ")
    
    matrix2text(datos, ruta_fichero)

# Definir función
def menu():
    print('a) Cargar fichero')
    print('b) Visualizar contenido del fichero')
    print('c) Visualizar promedio de edad y de estatura')
    print('d) Salir del programa')
    return input('Introduce una opción: ')

# Programa principal
ruta_fichero = crear_fichero()
opcion = menu()

while opcion != 'd':
    if opcion == 'a':
        carga_datos(ruta_fichero)
    elif opcion == 'b':
        matriz = text2matrix(ruta_fichero)
        for fila in matriz:
            print(fila)
    elif opcion == 'c':
        matriz = text2matrix(ruta_fichero)
        print('El promedio de edad es:', media_columna(matriz, 1))
        print('El promedio de estatura es:', media_columna(matriz, 2))
    else:
        print('Opción no válida')
    
    opcion = menu()

print('Fin del programa')
