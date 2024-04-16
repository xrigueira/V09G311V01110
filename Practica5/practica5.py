"""Una empresa de fabricación de frigoríficos tiene varias factorías, de las cuales tenemos la siguiente información:

• Ciudad en la que se ubica la fábrica.

• Número de unidades fabricadas el año pasado.

• Número de unidades defectuosas fabricadas el año pasado.

• Coste por unidad de cada frigorífico fabricado (en euros).

Por ejemplo:

Ciudad                  Producción total                 Defectuosas         Coste unitario (€)

Vigo                      731                                      23                         3498.54

Lugo                     238                                      12                         3823.35

A Coruña              801                                      26                         3324.12

Santiago               510                                      17                         3325.89

Realizar lo siguiente:

1.- Crear una matriz con datos fijos que contenga en cada fila la información de una fábrica, en el orden indicado en la lista anterior (pueden utilizarse los datos que figuran en la tabla de ejemplo).

2.- Presentar al usuario un menú que le permita elegir entre las siguientes opciones:

    i.   Añadir nueva fábrica

    ii.  Calcular la producción total conjunta

    iii. Calcular el total de unidades defectuosas

    iv.  Fábrica con menor % de piezas defectuosas

    v.   Visualizar fábricas que superan umbral de fabricación

    vi.  Salir del programa

En el diseño del programa se tendrán en cuenta las siguientes consideraciones:

En relación a la primera opción del menú, evitar introducir ciudades repetidas. En esos casos se notificará el error al usuario y no se pedirá el resto de la información de esa ciudad.
El programa funcionará mientras el usuario no decida salir.

Se utilizarán las siguientes funciones (almacenadas en un módulo propio):

Una función que, partiendo de una matriz y un nº de columna, devuelva la suma de los elementos de esa columna.

Una función que, partiendo de una matriz y un nº de columna, devuelva el mínimo de los elementos de esa columna.

Una función que, partiendo de una matriz, un nº de columna y un valor numérico, devuelva, en una lista, los elementos que, almacenados en la columna indicada de la matriz, superan el valor numérico indicado.

"""

# Importamos las funciones del modulo utils
from utils import *

# Definimos la matriz que contiene los datos
datos = [['Vigo', 731, 23, 3498.54],
        ['Lugo', 238, 12, 3823.35],
        ['A Coruña', 801, 26, 3324.12],
        ['Santiago', 510, 17, 3325.89]]

# Definir las opciones
opcion = 0
while opcion != 6:
    try:
        opcion = int(input("Elija una de las siguientes opciones\n1-     Añadir nueva fábrica\n2-     Calcular la producción total conjunta\n3-     Calcular el total de unidades defectuosas\n4-     Fábrica con menor % de piezas defectuosas\n5-     Visualizar fábricas que superan umbral de fabricación\n6-     Salir del programa\nTeclear opcion a continuacion: "))

        if opcion not in [1, 2, 3, 4, 5, 6]:
            print('Opcion no valida')

        if opcion in [1, 2, 3, 4, 5, 6]:
            print('Ha elegido la opcion numero', opcion)

        else:
            print('Hasta luego!')

        # Definir la opcion 1: añadir nueva fabrica no repetida
        if opcion == 1:
            try:
                ciudad = input('Introduzca la ciudad: ')
                if ciudad in [row[0] for row in datos]:
                    print('La ciudad ya existe')
                else:
                    produccion = int(input('Introduzca la produccion total: '))
                    defectuosas = int(input('Introduzca el numero de unidades defectuosas: '))
                    coste = float(input('Introduzca el coste unitario: '))
                    datos.append([ciudad, produccion, defectuosas, coste])
                    print('La ciudad ha sido añadida correctamente')
            except ValueError:
                print('Por favor, introduzca un valor numerico')
        
        # Definir la opcion 2. Calcular la produccion total conjunta
        elif opcion == 2:
            produccion_total = sum_column(datos, 1)
            print('La produccion total conjunta es', produccion_total)
            
        # Definir la opcion 3. Calcular el total de unidades defectuosas
        elif opcion == 3:
            unidades_defectuosas = sum_column(datos, 2)
            print('El total de unidades defectuosas es', unidades_defectuosas)
        
        # Definir la opcion 4. Fábrica con menor % de piezas defectuosas utilizando la función min_column
        elif opcion == 4:
            min_defectuosas = min_column(datos, 2)
            fabrica = []
            for row in datos:
                if row[2] == min_defectuosas:
                    fabrica.append(row[0])
            print('La fabrica con menor % de piezas defectuosas es', fabrica)
        
        # Definir la opcion 5. Visualizar fábricas que superan umbral de fabricación empleando la función elements_above
        elif opcion == 5:
            try:
                umbral = int(input('Introduzca el umbral de fabricacion: '))
                fabricas = elements_above(datos, 1, umbral)
                print('Las fabricas que superan el umbral de fabricacion son', fabricas)
            except ValueError:
                print('Por favor, introduzca un valor numerico')

    # En caso de que no se introduzca un numero
    except ValueError:
        print('Por favor, introduzca un numero entero')