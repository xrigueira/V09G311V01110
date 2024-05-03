
# #%% Read a file
# fichero = open("other/texto.txt", "r") # w -> write, r -> read, a -> append

# for line in fichero:
#     print(line)

# fichero.close()

# #%% Write a file
# fichero = open('other/numeros.txt', 'w')

# for i in range(0, 10):
#     fichero.write("Linea " + str(i) + "\n")

# fichero.close()

# #%% Append a file
# fichero = open('other/apendado.txt', 'a')
# fichero.write("\n")
# for i in range(10):
#     fichero.write("Nueva linea " + str(i) + "\n")

# fichero.close()

# #%% Read a file with 'with'
# with open('other/texto.txt', 'r+') as fichero:
#     for line in fichero:
#         print(line)

# #%% Problema 40: Escribe un archivo con los nombres de algunos alumnos de una clase.
# nombres = ['Juan', 'Pedro', 'María', 'Ana', 'Luis', 'Carlos', 'Sofía', 'Marta', 'Lucía', 'Pablo']
# # with open('other/alumnos.txt', 'w') as fichero:
# #     for nombre in nombres:
# #         fichero.write(nombre + "\n")

# fichero_40 = open('other/alumnos.txt', 'w', encoding='utf-8')
# for nombre in nombres:
#     fichero_40.write(nombre + "\n")
# fichero_40.close()

#%% Problema propuesto en clase:
import os
ruta = os.getcwd() + '\V09G311V01110\other'
print(ruta)

nombre = input('Nombre del fichero: ')
nomcompleto = ruta + '\\' + nombre + '.txt'
print(nomcompleto)

if os.path.exists(nomcompleto):
    fichero = open(nomcompleto, 'a')
else:
    fichero = open(nomcompleto, 'w')

introducir = True
while introducir:
    elige = input('¿Quieres introducir datos? (s/n): ').lower()
    if elige == 'n':
        introducir = False
        break
    dato_1 = input('Teclea un nombre: ')
    dato_2 = input('Teclea una estatura: ')
    fichero.write(dato_1 + ';' + dato_2 + '\n')
    elige = input('¿Quieres introducir más datos? (s/n): ').lower()
    if elige == 'n':
        introducir = False

fichero.close()

# Lee el fichero, mostrar 
with open(nomcompleto, 'r') as fichero:
    estaturas = 0
    for i, line in enumerate(fichero):
        datos = line.split(';')
        print(datos[0] + ' ' + datos[1])

        estaturas += int(datos[1])
    
    print('Media de estaturas: ', + (estaturas / (i + 1)))