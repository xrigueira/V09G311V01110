"""
Definir un programa en Python que permita cargar, modificar y listar datos de productos en un archivo.
El programa debe tener un menú con las siguientes opciones:

    1. Cargar nuevos datos en el archivo: 
    El usuario podrá ingresar el código, nombre, precio y cantidad en almacén de un producto y estos 
    datos se guardarán en el archivo.

    2. Modificar datos existentes en el archivo: 
    El usuario podrá seleccionar un producto del archivo y elegir si desea cambiar el precio o 
    la cantidad en almacén. Luego, podrá ingresar el nuevo valor y este se actualizará en el archivo.

    3. Listar todos los elementos del archivo: 
    El programa mostrará en pantalla todos los productos 
    almacenados en el archivo, mostrando su código, nombre, precio y cantidad.

    4. Salir del programa: 
    El programa finalizará su ejecución.

El programa debe permitir al usuario ingresar el nombre del archivo con el que desea trabajar. 
Si el archivo no existe, se creará automáticamente.
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
        codigo_producto = str(input("Dame el código del producto: "))
        nombre_producto = str(input("Dame el nombre del producto: ")) 
        precio = str(input("Dame el precio: "))
        cantidad_almacen = str(input("Dame la cantidad en almacén: "))
        datos.append([codigo_producto, nombre_producto, precio, cantidad_almacen])
        
        opcion_carga = input("¿Quieres meter más datos (n=no)? ")

    matrix2text(datos, ruta_fichero)

# Función de modificar datos
def modificar_fichero(ruta_fichero):
    
    # Leer los datos
    datos = text2matrix(ruta_fichero)
    
    cambio = str(input("¿Qué quieres cambiar el precio (p) o la cantidad en almacén (c) o nada(n)? " ))
    
    # Extraer los productos
    productos = []
    for producto in datos:
        productos.append(producto[1])
    
    if cambio.lower() == "p":
        producto = str(input("Dame el nombre del producto: "))
        if producto in productos:
            precio = str(input("Dame el precio: "))
            datos[productos.index(producto)][2] = precio
    
    elif cambio.lower() == "c":
        producto = str(input("Dame el nombre del producto: "))
        if producto in productos:
            cantidad = str(input("Dame la cantidad: "))
            datos[productos.index(producto)][3] = cantidad
    
    elif cambio.lower() == "n":
        print ("Sin cambios ")
    
    matrix2text(datos, ruta_fichero)

# Función de listado
def listado(nombre_fichero):
    
    # Abrir el fichero para leer datos
    fichero = open(nombre_fichero, 'r')
    for line in fichero:
        elementos = line.split(',')
        print ("Código: ", elementos[0], "Nombre: ", elementos[1], "Precio: ", elementos[2], "Cantidad: ", elementos[3])
    
    # Cerrar el fichero
    fichero.close()

# Menu principal
def menu():
    
    fichero = crear_fichero()
    opcion = ""
    while opcion.upper() != "F":
        try:
            # os.system("cls")
            opcion = input("\nMenú:\n   C)Cargar nuevos datos en el fichero\n   M)Modificar alguno de los datos del fichero (solo precio y cantidad)\n   L)Listar todos los elementos dle fichero\n   F)FIN\n   Teclear la opción a continuación: ")
            
            if opcion.upper() not in ["C", "M", "L", "F"]:
                print('Opción no válida')

            if opcion.upper() in ["C", "M", "L", "F"]:
                print('Ha elegido la opción:', opcion)

            if opcion.upper() == "C":
                carga_datos(fichero)
            
            elif opcion.upper() == "M":
                modificar_fichero(fichero)
            
            elif opcion.upper() == "L":
                listado(fichero)
            
            elif opcion.upper() == "F":
                print ("Fin de programa")
        
        
        except ValueError:
            print('Por favor, introduzca una cadena')

# Programa principal
menu()
