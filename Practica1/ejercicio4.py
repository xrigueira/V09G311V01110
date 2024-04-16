"""
Completa este programa para que calcule la letra de un dni:
"""

letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
dni = '39490825'
posicion = int(dni) % 23
print(posicion)
letra_dni = letras_dni[posicion]
NIF = dni + letra_dni
print("NIF = ",NIF)