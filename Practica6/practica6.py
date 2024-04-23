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

1.- Preguntar al usuario cuál es el fichero sobre el que se va a ejecutar el programa.

2.- Presentar al usuario un menú que le permita elegir entre las siguientes opciones:

    i.   Añadir nueva fábrica

    ii.  Calcular la producción total conjunta

    iii. Calcular el total de unidades defectuosas

    iv.  Fábrica con menor % de piezas defectuosas

    v.   Visualizar fábricas que superan umbral de fabricación

    vi.  Salir del programa

En el diseño del programa se tendrán en cuenta las siguientes consideraciones:

En relación al funcionamiento del programa, el programa debe advertir al usuario, al iniciar la ejecución, si  
existe ya almacenado un fichero con el nombre indicado. En caso afirmativo, se imprimirá la información que contiene 
el fichero antes de presentar el menú.

En relación a la primera opción del menú, evitar introducir ciudades repetidas. En esos casos se notificará el error 
al usuario y no se pedirá el resto de la información de esa ciudad.

"""

import os
# Importamos las funciones del modulo utils
from utils import *

# Definir las opciones
opcion = 0
while opcion != 6:
    
    # Preguntar al usuario cuál es el fichero sobre el que se va a ejecutar el programa
    ruta = os.getcwd() + '\Practica6'
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

    try:
      opcion = int(input("Elija una de las siguientes opciones\n1-     Añadir nueva fábrica\n2-     Calcular la producción total conjunta\n3-     Calcular el total de unidades defectuosas\n4-     Fábrica con menor % de piezas defectuosas\n5-     Visualizar fábricas que superan umbral de fabricación\n6-     Salir del programa\nTeclear opcion a continuacion: "))

      if opcion not in [1, 2, 3, 4, 5, 6]:
          print('Opcion no valida')
      
      if opcion in [1, 2, 3, 4, 5, 6]:
          print('Ha elegido la opcion', opcion)
      
      else:
          print('Hasta luego!')

      # Definir la opcion 1: añadir una nueva fábrica no repetida
      datos = text2matrix(ruta_fichero)
      
      if opcion == 1:
          try:
              ciudad = input('Introduzca la ciudad: ')
              if ciudad in [row[0] for row in datos]:
                  print('La ciudad ya existe')
              else:
                  produccion = input('Introduzca la produccion total: ')
                  defectuosas = input('Introduzca el numero de unidades defectuosas: ')
                  coste = input('Introduzca el coste unitario: ')
                  datos.append([ciudad, produccion, defectuosas, coste])
                  print('La ciudad ha sido añadida correctamente')

                  # Guardar los datos en el fichero
                  matrix2text(datos, ruta_fichero)

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