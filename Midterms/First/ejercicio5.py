"""
Diseña un programa que solicite al usuario el nombre de una institución u organización y devuelva su acrónimo. 
No se tendrán en cuenta para el acrónimo las palabras “de”, “del” o “y”. Además, visualizará el número de vocales 
que contiene el nombre de la institución.
"""

# Solicitar al usuario el nombre de una institución u organización
nombre = ""
while nombre == "":
    nombre = input("Introduce el nombre de una institución u organización: ")
    if nombre == "":
        print("El nombre no puede estar vacío")

# Calcular el acrónimo
palabras = nombre.split()
acronimo = ""
for palabra in palabras:
    if palabra.lower() not in ["de", "del", "y"]:
        acronimo += palabra[0].upper()
print(f"El acrónimo de {nombre} es {acronimo}")

# Calcular el número de vocales
vocales = 0
for letra in nombre:
    if letra.lower() in "aeiouáéíóú":
        vocales += 1
print(f"El nombre de la institución u organización {nombre} contiene {vocales} vocales")