"""
Diseñar un programa, en el que todas las partes se controlan con funciones y que contenga lo siguiente:

Un menú con la siguientes opciones

    1. Crear un fichero
    2. Meter datos en el fichero
    3. Leer del dichero y sumar
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

import os.path

def crear_fichero():

    # Acceder al directorio actual
    pass

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
        
        # Definir la opcion 1
        if opcion == 1:
            pass
        
        # Definir la opcion 2
        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

    # En caso de que no se introduzca un numero
    except ValueError:
        print('Por favor, introduzca un numero entero')