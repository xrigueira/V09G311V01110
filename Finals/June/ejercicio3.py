lista_dni = ["77389338L", "98859234J", "82993021M", "26205763T", "57570882L", "24501680X",
            "40890955Z", "27654661J", "09509875L", "03199116T", "58761263N"]

lista_notas = [3.4, 6.7, 5.0, 10, 2.4, 6.6, 6.789, 8.2, 4.8, 9.7, 7.5]

# Definir función para introducir nota
def introducir_nota(dni, nota, lista_dni, lista_notas):
    if dni in lista_dni:
        print("El DNI ya existe en la lista")
    else:
        lista_dni.append(dni)
        lista_notas.append(nota)
        print("Nota introducida con éxito")

# Definir función para listar notas
def listar_notas(lista_dni, lista_notas):
    for i in range(len(lista_dni)):
        print(f'El DNI {lista_dni[i]} ha sacado {lista_notas[i]}')

# Definir función para buscar nota
def buscar_nota(dni, lista_dni, lista_notas):
    if dni in lista_dni:
        print(f'La nota de {dni} es {lista_notas[lista_dni.index(dni)]}')
    else:
        print('El DNI no existe en la lista')

# Definir función para contar notas entre rangos
def contar_rangos_notas(lista_notas, limite_inferior, limite_superior):
    contador = 0
    for nota in lista_notas:
        if nota >= limite_inferior and nota <= limite_superior:
            contador += 1
    return contador

# Definir función para borrar nota
def borrar_nota(dni, lista_dni, lista_notas):
    if dni in lista_dni:
        lista_notas.pop(lista_dni.index(dni))
        lista_dni.remove(dni)
        print('Nota borrada con éxito')
    else:
        print('El DNI no existe en la lista')

# Definir función para modificar nota
def modificar_nota(dni, lista_dni, lista_notas):
    if dni in lista_dni:
        nueva_nota = float(input('Introduce la nueva nota: '))
        lista_notas[lista_dni.index(dni)] = nueva_nota
        print('Nota modificada con éxito')
    else:
        print('El DNI no existe en la lista')

# Menú de opciones
opcion = 0
while opcion != 7:

    try:
        opcion = int(input("Elija una de las siguientes opciones\n1-     Introducir nota\n2-     Listar notas\n3-     Buscar nota\n4-     Contar rangos de notas\n5-     Borrar nota\n6-     Modificar nota\nTeclear opcion a continuacion: "))

        if opcion not in [1, 2, 3, 4, 5, 6, 7]:
            print('Opcion no valida')
        
        if opcion in [1, 2, 3, 4, 5, 6, 7]:
            print('Ha elegido la opcion numero', opcion)
        
        else:
            print('Hasta luego')
        
        # Definir la opcion 1. Si nos saltamos la opción 1 el resto no funcionarán tal y como está planeado el ejercicio
        if opcion == 1:
            dni = input("Introduce el DNI: ")
            nota = float(input("Introduce la nota: "))
            introducir_nota(dni, nota, lista_dni, lista_notas)
        
        # Definir la opcion 2
        elif opcion == 2:
            listar_notas(lista_dni, lista_notas)
        
        # Definir la opcion 3
        elif opcion == 3:
            dni = input("Introduce el DNI: ")
            buscar_nota(dni, lista_dni, lista_notas)

        # Definir la opcion 4
        elif opcion == 4:
            limite_inferior = float(input("Introduce el límite inferior: "))
            limite_superior = float(input("Introduce el límite superior: "))
            contador = contar_rangos_notas(lista_notas, limite_inferior, limite_superior)
            print(f'Hay {contador} notas entre {limite_inferior} y {limite_superior}')

        # Definir la opcion 5
        elif opcion == 5:
            dni = input("Introduce el DNI: ")
            borrar_nota(dni, lista_dni, lista_notas)

        # Definir la opcion 6
        elif opcion == 6:
            dni = input("Introduce el DNI: ")
            modificar_nota(dni, lista_dni, lista_notas)
    
    # En caso de que no se introduzca un numero
    except ValueError:
        print('Por favor, introduzca un numero entero')