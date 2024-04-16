"""
Escribe un programa que calcule y muestre los 10 primeros valores de una tabla de
multiplicar que el usuario indique desde la consola. (“for” y “while”)
"""

num = int(input("What number do you want to work with: "))

multiplier = 0
while multiplier < 11:
    
    product = num * multiplier
    print(product)
    
    multiplier += 1