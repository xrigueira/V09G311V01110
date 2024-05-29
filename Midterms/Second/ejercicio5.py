"""
Define una función que, recibiendo como parámetros una cadena y un caracter concreto, devuelva, 
en una lista, las posiciones en las que se encuentra ese carácter dentro de la cadena.

En el programa principal, se asignará a una variable el valor “Ésta es la frase a adivinar”. 
Una vez hecho esto, se solicitará al usuario un caracter único (si no se introduce correctamente, 
se solicitará de nuevo) y, seguidamente, se llamará a la función para obtener la lista de posiciones 
en las que ese carácter aparece. Si el caracter introducido no se encuentra en la cadena, se visualizará 
el mensaje “El caracter introducido no forma parte del texto a averiguar”. Si se encuentra, se mostrarán 
las posiciones en las que aparece.
"""

# Definir función para obtener las posiciones de un caracter en una cadena
def posiciones_caracter(cadena, caracter):
    posiciones = []
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            posiciones.append(i)
    return posiciones

# Definir la frase a adivinar
cadena = "Ésta es la frase a adivinar"

# Solicitar al usuario un caracter único
caracter = input("Introduce un caracter: ")
while len(caracter) != 1:
    try:
        caracter = input("Introduce un caracter: ")
    except len(caracter) != 1:
        print("Introduce un solo caracter")

# Llamar a la función para obtener las posiciones en las que aparece el caracter
posiciones = posiciones_caracter(cadena, caracter)
if len(posiciones) == 0:
    print("El caracter introducido no forma parte del texto a averiguar")
else:
    print("El caracter", caracter, "se encuentra en las posiciones", posiciones)
