"""
Escribe un programa que mediante un menú se seleccione si se debe calcular el área o el
perímetro de un círculo. Seguidamente, el usuario debe introducir el valor del radio y se
muestra el resultado en la pantalla.
"""
import math

param = input('Que quieres calcular:\n1.Area\n2.Perimetro\n ')
radio = int(input('Cual es el valor del radio: '))

if param == 'area':
    print('El area es:', math.pi*pow(radio,2))

else:
    print('El perimetro es:', 2*math.pi*radio)