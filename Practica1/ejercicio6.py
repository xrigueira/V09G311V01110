"""
Las siguientes líneas genera un número aleatorio entre 0 y 9:
"""

import random
num = random.randint(0, 9)

"""
Escribe un programa que, tras generar un número aleatorio, solicite al usuario un número
por teclado. El programa debe informar al usuario si ha acertado, o, en caso contrario, si
el número secreto es menor o mayor que el número introducido por el usuario.
"""

# Ask user for input
user_num = int(input("Dame un numero: "))

if num == user_num:
    print('Has acertado')

elif num > user_num:
    print('El número aleatorio es mayor')

elif num < user_num:
    print('El número aleatorio es menor')