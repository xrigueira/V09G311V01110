
"""Escribe un programa que simule un juego en el que dos jugadores 
lanzan su propio dado. El programa generará un número entero al 
azar entre 1 y 6 para cada jugador y mostrará el valor obtenido en 
el lanzamiento y el total obtenido hasta ese instante por cada jugador. 
Tras cada tirada se preguntará a cada uno de los jugadores si quieren 
volver a lanzar el dado o si desean terminar su partida. A partir del 
instante en que un jugador haya decidido no jugar, el programa no debe 
volver a preguntarle.

El programa debe continuar hasta que ambos jugadores decidan no jugar 
o hasta que uno de ellos supere los 21 puntos. Una vez finalizado el 
juego, el programa deberá declarar como ganador al jugador que haya 
obtenido más puntos sin superar los 21 puntos. Si ambos jugadores tienen 
una misma puntuación menor de 21, el programa deberá declarar un empate. 
Si ambos jugadores superan los 21 puntos, el programa deberá declarar 
que ambos perdieron.
"""

import random

#%% Solucion

# Solucion

# Inicialización de los totales de ambos jugadores
total_jugador_1 = 0
total_jugador_2 = 0

# Bucle del juego
while True:
    # Jugador 1
    respuesta_jugador_1 = input("¿Jugador 1, quieres lanzar de nuevo? (S/n): ").lower()
    if respuesta_jugador_1 != 's':
        print("El jugador 1 decide no jugar más.")
        break
    else:
        lanzamiento_jugador_1 = random.randint(1, 6)
        total_jugador_1 += lanzamiento_jugador_1
        print(f"El jugador 1 lanzó un {lanzamiento_jugador_1}. Total acumulado: {total_jugador_1}")

    # Verificar si el jugador 1 ya superó 21 puntos
    if total_jugador_1 > 21:
        break

    # Jugador 2
    respuesta_jugador_2 = input("¿Jugador 2, quieres lanzar de nuevo? (S/n): ").lower()
    if respuesta_jugador_2 != 's':
        print("El jugador 2 decide no jugar más.")
        break
    else:
        lanzamiento_jugador_2 = random.randint(1, 6)
        total_jugador_2 += lanzamiento_jugador_2
        print(f"El jugador 2 lanzó un {lanzamiento_jugador_2}. Total acumulado: {total_jugador_2}")

    # Verificar si el jugador 2 ya superó 21 puntos
    if total_jugador_2 > 21:
        break

# Determinar al ganador
if total_jugador_1 > 21 and total_jugador_2 > 21:
    print("Ambos jugadores perdieron, ¡qué mala suerte!")
elif total_jugador_1 > 21:
    print("¡El jugador 2 gana!")
elif total_jugador_2 > 21:
    print("¡El jugador 1 gana!")
else:
    if total_jugador_1 > total_jugador_2:
        print("¡El jugador 1 gana!")
    elif total_jugador_2 > total_jugador_1:
        print("¡El jugador 2 gana!")
    else:
        print("¡Empate!")

