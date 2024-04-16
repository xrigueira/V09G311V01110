"""
Diseña un programa que almacene, en dos listas distintas, los nombres y calificaciones del primer parcial de “Informática para la ingeniería”. El programa debe solicitar los datos hasta que el usuario 
indique que no desea introducir más. Debe asegurarse también de que se introduce una nota correcta (entre 0 y 10).

Una vez almacenados los datos en las listas, el programa presentará al usuario un menú similar al siguiente:

    Buscar calificación
    Modificar calificación
    Generar acta
    Alumnado con materia superada
    Alumnado que podrá hacer media
    Salir del programa

Comentarios:

Si se ejecuta la opción 1, el programa solicitará al usuario el nombre de la persona cuya calificación desea consultar. Si esa persona no está en el listado, se visualizará un mensaje indicándolo. 
En caso contrario, el programa imprimirá la calificación que le corresponde.

Si se ejecuta la opción 2, el programa solicitará al usuario el nombre de la persona cuya calificación desea modificar. Si esa persona no está en el listado, se visualizará un mensaje indicándolo. 
En caso contrario, el programa solicitará la nueva calificación y la almacenará en el lugar que le corresponde.

Al ejecutar la opción 3, el programa creará una matriz de dos dimensiones que almacenará, en su primera columna, los nombres del alumnado y, en la segunda columna, sus notas. Luego, la imprimirá, 
visualizando en cada línea los datos de una persona.

Si se ejecuta la opción 4, el programa creará una matriz de dos dimensiones similar a la del punto 3, pero sólo se incluirán en ella los datos del alumnado que ha superado la prueba.

Si se ejecuta la opción 5, el programa creará una matriz de dos dimensiones similar a la del punto 3, pero sólo se incluirán en ella los datos del alumnado que podrá hacer media (nota superior a 4).

El programa finalizará cuando el usuario elija la opción 6.
Si se elige una opción distinta de las presentadas, se imprimirá un mensaje de error.

VERSIÓN CON FUNCIONES

Implementa las opciones del menú del programa anterior definiendo y llamando a las siguientes funciones:

i) Una primera función que imprima el menú y devuelva como resultado la opción elegida por el usuario.
Esta función será llamada en el momento de presentar el menú al usuario para que elija entre sus opciones.

ii) Una segunda función que, dada una lista L y un elemento E, devuelva un dato de tipo lógico que tomará el valor verdadero (True) si el elemento dado se encuentra entre los elementos de la lista y 
falso (False) en caso contrario.

Esta función se llamará en las dos primeras opciones del menú.

iii) Una tercera función que, dadas dos listas L1 y L2 de la misma longitud, y un umbral, construya una matriz en la que cada una de las filas está formada por los elementos que ocupan la misma posición 
en las listas de partida, siempre y cuando el valor numérico en la segunda lista sea superior al umbral dado.

Por ejemplo, para las listas L1=[“Ana”,”Pedro”,”Luis”] y L2=[6,2,8] y un umbral=3, la matriz resultante sería:  [[“Ana”,6],[“Luis”,8]]

Esta función se llamará para resolver los apartados 3, 4 y 5 del menú.
"""

# Definier la función de menú
def menu():
    """Imprime el menú y devuelve la opción elegida por el usuario.
    ----------
    Args:
    None
    
    Returns:
    opcion (int): La opción elegida por el usuario."""
    
    opcion = int(input("Elija una de las siguientes opciones\n1-     Buscar calificación\n2-     Modificar calificación\n3-     Generar acta\n4-     Alumnado con materia superada\n5-     Alumnado que podrá hacer media\n6-     Salir del programa\nTeclear opcion a continuacion: "))

    return opcion

# Definir la función de búsqueda en una lista
def buscar_elemento(E, L):
    """Devuelve un dato de tipo lógico que toma el valor verdadero (True) 
    si el elemento dado se encuentra entre los elementos de la lista y falso 
    (False) en caso contrario.
    ----------
    Args:
    E (str): Elemento que se buscará en la lista.
    L (list): Lista en la que se buscará el elemento.
    
    Returns:
    bool: True si el elemento se encuentra en la lista, False en caso contrario."""
    
    return E in L

# Definir la de generación de acta
def generar_acta(L1, L2, umbral):
    """Construye una matriz en la que cada una de las filas está formada por los elementos 
    que ocupan la misma posición en las listas de partida, siempre y cuando el valor numérico 
    en la segunda lista sea superior al umbral dado.
    ----------
    Args:
    L1 (list): Lista de nombres.
    L2 (list): Lista de notas.
    umbral (int): Umbral de notas.

    Returns:
    acta (list): Matriz con los nombres y notas de los alumnos cuyas notas superan el umbral."""

    acta = [[L1[i], L2[i]] for i in range(len(L1)) if L2[i] >= umbral]

    return acta

if __name__ == '__main__':

    # Definir las variables necesarias
    nombres = []
    notas = []

    continuar = 's'
    # Recibir los datos
    while continuar == 's':
        try:
            # Recibir el nombre del alumno
            nombres.append(input('Introduzca el nombre del alumno: '))

            # Recibir la nota del alumno
            nota = -1
            while nota < 0 or nota > 10:
                try:
                    nota = int(input('Introduzca una calificacion: '))
                    if nota < 0 or nota > 10:
                        print('Por favor, introduzca una calificacion entre 0 y 10')
                    else:
                        notas.append(nota)
                except ValueError:
                    print('Por favor, introduzca una calificacion entre 0 y 10')

            # Preguntar si se desea introducir más datos
            continuar = input('Desea introducir otro numero? (s/n): ')

        except ValueError:
            print('Por favor, introduzca un número entero')

    # nombres = ['Juan', 'Pedro', 'Maria', 'Ana', 'Luis']
    # notas = [5, 6, 3, 4, 9]

    # Definir las opciones
    opcion = 0
    while opcion != 6:
        try:
            # First function call
            opcion = menu()

            if opcion not in [1, 2, 3, 4, 5, 6]:
                print('Opcion no valida')

            if opcion in [1, 2, 3, 4, 5]:
                print('Ha elegido la opcion numero', opcion)

            else:
                print('Hasta luego!')

            # Definir la opcion 1
            if opcion == 1:
                nombre = input('Introduzca el nombre del alumno: ')
                if buscar_elemento(nombre, nombres):
                    print('La calificacion de', nombre, 'es', notas[nombres.index(nombre)])
                else:
                    print('El alumno', nombre, 'no se encuentra en la lista')
            
            # Definir la opcion 2
            elif opcion == 2:
                nombre = input('Introduzca el nombre del alumno: ')
                if buscar_elemento(nombre, nombres):
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
                acta = generar_acta(nombres, notas, 0)
                print(acta)
            
            # Definir la opcion 4
            elif opcion == 4:
                acta = generar_acta(nombres, notas, 5)
                print(acta)
            
            # Definir la opcion 5
            elif opcion == 5:
                acta = generar_acta(nombres, notas, 4)
                print(acta)

        # En caso de que no se introduzca un numero
        except ValueError:
            print('Por favor, introduzca un numero entero')