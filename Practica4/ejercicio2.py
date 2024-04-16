"""
Supongamos que disponemos de dos listas que almacenan, respectivamente, nombres y teléfonos de una agenda. El nombre cuyo nombre ocupa una posición en la primera lista, se corresponde con el 
teléfono que se almacena en la misma posición en la segunda de las listas.

nombres=["JUAN","ANABEL","JAVIER","SABELA"]

tlfs=["603234567","678987654","698453212","986543210"]

Diseña un programa que, partiendo de la creación y almacenamiento de las listas anteriores, presente al usuario un menú que le permita:

1) Añadir una nueva persona a la agenda

2) Buscar por nombre

3) Buscar por teléfono

4) Visualizar la agenda

5) Salir del programa

Para implementar estas opciones se diseñarán las siguientes funciones:

I) Una función que, partiendo de una lista y un elemento, devuelva como resultado la posición en la que ese elemento se encuentra dentro de la lista.

II) Una función que, partiendo de una lista y una posición, devuelva como resultado el elemento de la lista que ocupa esa posición.

III) Una función que, partiendo de dos listas de idéntico número de elementos, devuelva una cadena con la correspondencia entre sus elementos.

En el programa principal se llamará a las distintas funciones para obtener los resultados; resultados que se imprimirán en el programa principal.
"""

def buscar_por_nombre(lista, elemento):
    """
    Devuelve la posicion de un elemento en una lista
    ----------
    Args:
    lista (list): Lista de elementos en la que buscar
    elemento (str): Elemento a buscar en la lista
    
    Returns:
    posicion (int): Posicion del elemento en la lista
    """

    if elemento in lista:
        return lista.index(elemento)
    else:
        return -1

def buscar_por_posicion(lista, posicion):
    """
    Devuelve el elemento de una lista que ocupa una posicion
    """

    if posicion < len(lista):
        return lista[posicion]
    else:
        return -1

def correspondencia_listas(lista1, lista2):

    """
    Devuelve una cadena con la correspondencia entre los elementos de dos listas
    ----------
    Args:
    lista1 (list): Lista de elementos
    lista2 (list): Lista de elementos

    Returns:
    cadena (str): Cadena con la correspondencia entre los elementos de las listas
    """

    cadena = ""

    for i in range(len(lista1)):
        cadena += lista1[i] + ": " + lista2[i] + "\n"

    return cadena

nombres = ["Juan", "Anabel", "Javier", "Sabela"]

tlfs = ["603234567", "678987654", "698453212", "986543210"]

if __name__ == '__main__':

    # Definir las opciones
    opcion = 0
    while opcion != 5:
        try:
            # First function call
            opcion = int(input("Elija una de las siguientes opciones\n1-     Añadir una nueva persona a la agenda\n2-     Buscar por nombre\n3-     Buscar por teléfono\n4-     Visualizar la agenda\n5-     Salir del programa\nTeclear opcion a continuacion: "))

            if opcion not in [1, 2, 3, 4, 5]:
                print('Opcion no valida')

            if opcion in [1, 2, 3, 4, 5]:
                print('Ha elegido la opcion numero', opcion)

            else:
                print('Hasta luego!')

            # Definir la opcion 1
            if opcion == 1:
                nombre = input('Introduzca el nombre de la persona: ')
                tlf = input('Introduzca el telefono de la persona: ')

                nombres.append(nombre)
                tlfs.append(tlf)
            
            # Definir la opcion 2
            elif opcion == 2:
                nombre = input('Introduzca el nombre de la persona: ')
                posicion = buscar_por_nombre(nombres, nombre)
                if posicion != -1:
                    print('El telefono de', nombre, 'es', buscar_por_posicion(tlfs, posicion))
                else:
                    print('El nombre no se encuentra en la lista')
            
            # Definir la opcion 3
            elif opcion == 3:
                tlf = input('Introduzca el telefono de la persona: ')
                posicion = buscar_por_nombre(tlfs, tlf)
                if posicion != -1:
                    print('El nombre de la persona con telefono', tlf, 'es', buscar_por_posicion(nombres, posicion))
                else:
                    print('El telefono no se encuentra en la lista')
            
            # Definir la opcion 4
            elif opcion == 4:
                print(correspondencia_listas(nombres, tlfs))
        
        # En caso de que no se introduzca un numero
        except ValueError:
            print('Por favor, introduzca un numero entero')
