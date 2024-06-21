"""
Diseñar un programa que solicite al usuario un número entero positivo (si el dato introducido no es correcto, 
volverá a solicitarse hasta su correcta introducción). Luego, dado ese número N, el programa comprobará que se 
cumple la siguiente igualdad, visualizando el cálculo de cada uno de los dos términos: 1^3+2^3+3^3+...+N^3 = (1+2+3+...+N)^2
"""

# Solicitar al usuario un número entero positivo
numero = 0
while numero <= 0:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero <= 0:
            print("El número debe ser positivo")
    except ValueError:
        print("El dato introducido no es correcto")

# Calcular la suma de los cubos de los números del 1 al N
suma_cubos = 0
for i in range(1, numero + 1):
    suma_cubos += i ** 3
    print(f"Suma primer termino: {suma_cubos}")

# Calcular el cuadrado de la suma de los números del 1 al N
suma = 0
for i in range(1, numero + 1):
    suma += i

cuadrado_suma = suma ** 2
print(f"Suma segundo termino: {cuadrado_suma}")

# Comprobar si se cumple la igualdad
if suma_cubos == cuadrado_suma:
    print(f"Se cumple la igualdad: 1^3+2^3+3^3+...+{numero}^3 = (1+2+3+...+{numero})^2")
else:
    print(f"No se cumple la igualdad: 1^3+2^3+3^3+...+{numero}^3 != (1+2+3+...+{numero})^2")