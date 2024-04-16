"""
El siguiente programa solicita al usuario que introduzca el radio de un círculo por teclado y
calcula su superficie:
"""

r = float(input("Radio del círculo: "))

a = 3.1416*r**2

print("Área: " + str(a))

"""
Implementar un programa similar que pregunte el precio base (sin IVA) de una entrada de
cine, y calcule los precios añadiendo el 10 % y 21 % de IVA. Estimar el ahorro debido a la
bajada de impuestos
"""

precio = int(input("Cuál es el precio base de la entrada de cine: "))

precio_10 = precio * 1.10

precio_21 = precio * 1.21

savings = precio_21 - precio_10

print(f'{savings} € de ahorro')