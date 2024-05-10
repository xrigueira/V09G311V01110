"""
Diseñar un programa, en el que todas las partes se controlan con funciones y que contenga lo siguiente:

Un menú con la siguientes opciones

    1. Crear un fichero
    2. Meter datos en el fichero
    3. Leer de dichero y sumar
    4. Fin

En la opción 1 se creará el fichero con el nombre y dirección que indique el usuario y, además,
se comprobará si existe o no, si existe NO se podrá generar de nuevo.

En la opción 2 se meterán tres tipos de datos en el fichero:
    Nombre del mineral;Peso atómico;Precio;precio/Kg

En la opción 3 se leerán los datos del fichero, sumando el precio para los Kg que diga el usuario
para todos los productos, generando un informe del siguiente tipo

    Kilogramos a calcular 10
    Nombre del mineral      Peso atómico        Precio/kg       Total
    Oro                     196.996             59148.00        591480.00
    Plata                   107.868             703.75          7037.50
    Titanio                 47.867              139.50          1395.00
    Total:------------------------------------------------------599912.50

Si el usuario teclea un valor fuera de lugar el sistema debe indicarlo.
En cualquier otra opción se debe visualizar un mensaje de error.

Nota importante: se evaluará que las funciones reciban parámetros y devuelvan algún tipo de dato.
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

# Definir función para crear el fichero en caso de que no exista
def crear_fichero():

    # Preguntar al usuario cuál es el fichero sobre el que se va a ejecutar el programa
    ruta = os.getcwd() + '\\Finals\\June'
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
        nombre_mineral = str(input("Dame el nombre del mineral: "))
        codigo_mineral = str(input("Dame el peso atómico: ")) 
        precio = str(input("Dame el precio/kg: "))
        datos.append([nombre_mineral, codigo_mineral, precio])
        
        opcion_carga = input("¿Quieres meter más datos (n=no)? ")

    matrix2text(datos, ruta_fichero)

def generar_informe(ruta_fichero):
    
    # Leer los datos
    datos = text2matrix(ruta_fichero)

    # Preguntar al usuario cuántos kilogramos se van a calcular
    kilogramos = int(input('Kilogramos a calcular: '))

    # Multiplicar el precio por kilogramo por la cantidad de kilogramos y añadirlo a la matriz en la última columna
    for producto in datos:
        producto.append(str(float(producto[2]) * kilogramos))
    
    # Imprimir el informe
    print('Nombre del mineral\tPeso atómico\tPrecio/kg\tTotal')
    for producto in datos:
        print('\t'.join(producto))

    # Calcular el total
    total = 0
    for producto in datos:
        total += float(producto[3])
    print('Total-------------------------------------------', total)
# Menú de opciones
opcion = 0
while opcion != 4:

    try:
        opcion = int(input("Elija una de las siguientes opciones\n1-     Crear un fichero\n2-     Meter datos en el fichero\n3-     Leer del fichero y sumar\n4-     Salir del programa\n\nTeclear opcion a continuacion: "))

        if opcion not in [1, 2, 3, 4]:
            print('Opcion no valida')
        
        if opcion in [1, 2, 3, 4]:
            print('Ha elegido la opcion numero', opcion)
        
        else:
            print('Hasta luego')
        
        # Definir la opcion 1. Si nos saltamos la opción 1 el resto no funcionarán tal y como está planeado el ejercicio
        if opcion == 1:
            fichero = crear_fichero()
        
        # Definir la opcion 2
        elif opcion == 2:
            carga_datos(ruta_fichero=fichero)

        elif opcion == 3:
            generar_informe(ruta_fichero=fichero)

    # En caso de que no se introduzca un numero
    except ValueError:
        print('Por favor, introduzca un numero entero')