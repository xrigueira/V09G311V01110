"""
Diseña un programa que almacene, en dos listas distintas, los nombres y calificaciones del primer parcial de “Informática para la ingeniería”. 
El programa debe solicitar los datos hasta que el usuario indique que no desea introducir más. Debe asegurarse también de que se introduce 
una nota correcta (entre 0 y 10).

Una vez almacenados los datos en las listas, el programa presentará al usuario un menú similar al siguiente:

    1. Buscar calificación
    2. Modificar calificación
    3. Generar acta
    4. Alumnado con materia superada
    5. Alumnado que podrá hacer media
    6. Salir del programa

Comentarios:

Si se ejecuta la opción 1, el programa solicitará al usuario el nombre de la persona cuya calificación desea consultar. 

Si esa persona no está en el listado, se visualizará un mensaje indicándolo. En caso contrario, el programa imprimirá la calificación 
que le corresponde.

Si se ejecuta la opción 2, el programa solicitará al usuario el nombre de la persona cuya calificación desea modificar. Si esa persona 
no está en el listado, se visualizará un mensaje indicándolo. En caso contrario, el programa solicitará la nueva calificación y la almacenará 
en el lugar que le corresponde.

Al ejecutar la opción 3, el programa creará una matriz de dos dimensiones que almacenará, en su primera columna, los nombres del alumnado y, 
en la segunda columna, sus notas. Luego, la imprimirá, visualizando en cada línea los datos de una persona.

Si se ejecuta la opción 4, el programa creará una matriz de dos dimensiones similar a la del punto 3, pero sólo se incluirán en ella los 
datos del alumnado que ha superado la prueba.

Si se ejecuta la opción 5, el programa creará una matriz de dos dimensiones similar a la del punto 3, pero sólo se incluirán en ella los 
datos del alumnado que podrá hacer media (nota superior a 4).

El programa finalizará cuando el usuario elija la opción 6.

Si se elige una opción distinta de las presentadas, se imprimirá un mensaje de error.

"""

# # Definir las variables necesarias
# nombres = []
# notas = []

# continuar = 's'
# # Recibir los datos
# while continuar == 's':
#     try:
#         # Recibir el nombre del alumno
#         nombres.append(input('Introduzca el nombre del alumno: '))

#         # Recibir la nota del alumno
#         nota = -1
#         while nota < 0 or nota > 10:
#             try:
#                 nota = int(input('Introduzca una calificacion: '))
#                 if nota < 0 or nota > 10:
#                     print('Por favor, introduzca una calificacion entre 0 y 10')
#                 else:
#                     notas.append(nota)
#             except ValueError:
#                 print('Por favor, introduzca una calificacion entre 0 y 10')

#         # Preguntar si se desea introducir más datos
#         continuar = input('Desea introducir otro numero? (s/n): ')

#     except ValueError:
#         print('Por favor, introduzca un número entero')

nombres = ['Juan', 'Pedro', 'Maria', 'Ana', 'Luis']
notas = [5, 6, 3, 4, 9]

# Definir las opciones
opcion = 0
while opcion != 6:
    try:
        opcion = int(input("Elija una de las siguientes opciones\n1-     Buscar calificación\n2-     Modificar calificación\n3-     Generar acta\n4-     Alumnado con materia superada\n5-     Alumnado que podrá hacer media\n6-     Salir del programa\nTeclear opcion a continuacion: "))

        if opcion not in [1, 2, 3, 4, 5, 6]:
            print('Opcion no valida')

        if opcion in [1, 2, 3, 4, 5]:
            print('Ha elegido la opcion numero', opcion)

        else:
            print('Hasta luego!')

        # Definir la opcion 1
        if opcion == 1:
            nombre = input('Introduzca el nombre del alumno: ')
            if nombre in nombres:
                print('La calificacion de', nombre, 'es', notas[nombres.index(nombre)])
            else:
                print('El alumno', nombre, 'no se encuentra en la lista')
        
        # Definir la opcion 2
        elif opcion == 2:
            nombre = input('Introduzca el nombre del alumno: ')
            if nombre in nombres:
                nota = -1
                while nota < 0 or nota > 10:
                    try:
                        nota = int(input('Introduzca una calificacion: '))
                        if nota < 0 or nota > 10:
                            print('Por favor, introduzca una calificacion entre 0 y 10')
                        else:
                            notas[nombres.index(nombre)] = nota
                    except ValueError:
                        print('Por favor, introduzca una calificacion entre 0 y 10')
            else:
                print('El alumno', nombre, 'no se encuentra en la lista')
            
        # Definir la opcion 3
        elif opcion == 3:
            acta = [[nombres[i], notas[i]] for i in range(len(nombres))]
            # Without using a list comprehension
            # acta = []
            # for i in range(len(nombres)):
            #     acta.append([nombres[i], notas[i]])
            print(acta)
        
        # Definir la opcion 4
        elif opcion == 4:
            acta = [[nombres[i], notas[i]] for i in range(len(nombres)) if notas[i] >= 5]
            print(acta)
        
        # Definir la opcion 5
        elif opcion == 5:
            acta = [[nombres[i], notas[i]] for i in range(len(nombres)) if notas[i] > 4]
            print(acta)

    # En caso de que no se introduzca un numero
    except ValueError:
        print('Por favor, introduzca un numero entero')