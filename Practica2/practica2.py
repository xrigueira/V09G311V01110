"""Diseña un programa que presente al usuario el siguiente menú:

1-     Crear lista de enteros

2-     Visualizar pares

3-     Visualizar impares

4-     Finalizar el programa

Elige una opción:

El usuario podrá ejecutar las diferentes opciones del menú tantas veces como lo desee, hasta que decida salir eligiendo la opción 4 del menú.

Comentarios:

Cuando el usuario elige la opción 1, el programa pedirá datos enteros al usuario hasta que éste decida no introducir más. 
Estos enteros se irán almacenando en una lista. El programa debe controlar la validez del dato introducido por el usuario 
antes de almacenarlo en la lista. Una vez introducido correctamente un dato, se preguntará al usuario si desea introducir alguno más.

Cuando el usuario elige la opción 2, el programa visualizará los datos almacenados en la lista que son pares.

Cuando el usuario elige la opción 3, el programa visualizará los datos almacenados en la lista que son impares.

Cuando el usuario elige la opción 4 finaliza el programa.

Si el usuario elije alguna opción distinta a las presentadas, se visualizará un mensaje de error.

El programa no podrá ejecutar las opciones 2 y 3 si, previamente, al menos una vez, no se ha ejecutado la opción 1. Si el usuario lo intenta, 
se le mostrará un mensaje que le indique que no se han introducido datos."""

# Definir el menú
opcion = 0
while opcion != 4:
    
    # Intentar recibir la opcion
    try:
        opcion = int(input("Elija una de las siguientes opciones\n1-     Crear lista de enteros\n2-     Visualizar pares\n3-     Visualizar impares\n4-     Finalizar el programa\nTeclear opcion a continuacion: "))

        # Exceptuar si la opcion no es valida. Es decir no es uno de los 4 numeros posibles
        if opcion not in [1, 2, 3, 4]:
            raise Exception("Opción no válida")
        
        if opcion in [1, 2, 3]:
            print('Ha elegido la opción numero', opcion)
        
        elif opcion == 4:
            print('Hasta luego!')
            break
        
        # Definir la opcion 1
        if opcion == 1:
            lista = []
            while True:
                try:
                    dato = int(input('Introduzca un número entero: '))
                    lista.append(dato)
                    continuar = input('¿Desea introducir otro número? (s/n): ')
                    if continuar.lower() != 's':
                        break
                except ValueError:
                    print('Por favor, introduzca un número entero')
                    continue
        
        # Definir la opcion 2
        elif opcion == 2:
            try:
                print('Los números pares son: ', [i for i in lista if i % 2 == 0])
            except NameError:
                print('No se han introducido datos')
                continue
        
        # Definir la opcion 3
        elif opcion == 3:
            try:
                print('Los números impares son: ', [i for i in lista if i % 2 != 0])
            except NameError:
                print('No se han introducido datos')
                continue
    
    # En caso de que no se introduzca un número
    except ValueError:
        print('Por favor, introduzca un número entero')
        continue


