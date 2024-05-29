"""
Disponemos de un fichero que almacena las calificaciones de las personas que se presentaron a un examen para una materia determinada. Ejemplo de este fichero podría ser:
    
    58788987Y;Pedro Fernández Arias;7.8
    67896521B;Ana Acosta Pérez;3.5
    43231097M;Inés García Couso;9

Diseñar un programa que permita al usuario 
    
    1)	Buscar la nota de un alumno o alumna, introduciendo su DNI.
    2)	Almacenar en un segundo fichero, cuyo nombre se preguntará al usuario, la información de las personas que han superado la materia. Si el nombre dado por el usuario ya existiese, se advertirá al usuario y se le preguntará si quiere reemplazarlo.
    3)	Calcular la nota media y el número de personas que se presentaron al examen.
    4)	Salir del programa
"""
import os

# Función para transformar un fichero de texto en una matriz.
def text2matrix(filepath):
    matrix = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip().split(';')
            matrix.append(list(line))
    return matrix

# Función para transformar una matriz en un fichero de texto.
def matrix2text(matrix, filepath):
    with open(filepath, 'w') as file:
        for row in matrix:
            file.write(','.join(row) + '\n')

# Función para buscar la nota de un alumno o alumna, introduciendo su DNI
def buscar_nota_alumx_por_DNI(DNI, filepath):
    datos = text2matrix(filepath)
    for dato in datos:
        if DNI in dato:
            return dato[2]
    return 'No se ha encontrado el DNI'

# Definir función para crear el fichero en caso de que no exista
def crear_fichero():

    # Preguntar al usuario cuál es el fichero sobre el que se va a ejecutar el programa
    ruta = os.getcwd() + '\\Midterms\\Second'
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

# Función para almacenar en un segundo fichero la información de las personas que han superado la materia
def almacenar_aprobados(filepath_old, filepath_new):
    datos = text2matrix(filepath_old) # Leer el fichero
    
    # Crear una matriz con los aprobados
    aprobados = []
    for dato in datos:
        if float(dato[2]) >= 5:
            aprobados.append(dato)
    
    # Guardar la matriz en un fichero
    matrix2text(aprobados, filepath=filepath_new)

# Función para calcular la nota media y el número de personas que se presentaron al examen
def nota_media_presentados(filepath):
    datos = text2matrix(filepath) # Leer el fichero

    # Calcular la nota media
    suma = 0
    for dato in datos:
        suma += float(dato[2])
    
    nota_media = suma / len(datos)

    # Calcular el número de personas que se presentaron al examen
    presentados = len(datos)

    return nota_media, presentados

# Menú de opciones
opcion = 0
while opcion != 4:

    try:
        opcion = int(input("Elija una de las siguientes opciones\n1-     Buscar nota alumx por DNI\n2-     Almacenar en segundo fichero la infomación de los aprobados\n3-     Calcular la nota media y el número de personas que se presentaron al examen\n4-     Salir del programa\n\nTeclear opcion a continuacion: "))

        if opcion not in [1, 2, 3, 4]:
            print('Opcion no valida')
        
        if opcion in [1, 2, 3, 4]:
            print('Ha elegido la opcion numero', opcion)
        
        else:
            print('Hasta luego')
        
        # Definir la opcion 1
        if opcion == 1:
            filepath = 'Midterms\\Second\\notas.txt'
            dni = input('Introduzca el DNI del alumno o alumna: ')
            print(buscar_nota_alumx_por_DNI(dni, filepath))
        
        # Definir la opcion 2
        elif opcion == 2:
            filepath_old = 'Midterms\\Second\\notas.txt' # Fichero original
            filepath_new = crear_fichero() # Definir el fichero nuevo
            almacenar_aprobados(filepath_old, filepath_new) # Almacenar los aprobados en el fichero nuevo

        elif opcion == 3:
            filepath = 'Midterms\\Second\\notas.txt'
            nota_media, presentados = nota_media_presentados(filepath)
            print('La nota media es:', nota_media)
            print('El número de personas que se presentaron al examen es:', presentados)

    # En caso de que no se introduzca un numero
    except ValueError:
        print('Por favor, introduzca un numero entero')