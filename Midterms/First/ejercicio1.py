"""
Diseñar un programa que solicite al usuario un número entero positivo (si el dato introducido no es correcto, 
volverá a solicitarse hasta su correcta introducción). Luego, mostrará en pantalla si el número introducido es par o 
impar, cuántas cifras tiene y cuál es la suma de sus cifras
"""

# # Solicitar al usuario un número entero positivo
# while True:
#     try:
#         numero = int(input("Introduce un número entero positivo: "))
#         if numero > 0:
#             break
#         else:
#             print("El número debe ser positivo")
#     except ValueError:
#         print("El dato introducido no es correcto")

# Solicitar al usuario un número entero positivo
numero = 0
while numero <= 0:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero <= 0:
            print("El número debe ser positivo")
    except ValueError:
        print("El dato introducido no es correcto")

# Mostrar si el número introducido es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

# Mostrar cuántas cifras tiene el número introducido
cifras = len(str(numero))
print(f"El número {numero} tiene {cifras} cifras")

# Mostrar la suma de las cifras del número introducido
suma = 0
for cifra in str(numero):
    suma += int(cifra)
print(f"La suma de las cifras del número {numero} es {suma}")

