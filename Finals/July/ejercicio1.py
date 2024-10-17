"""Diseña una primera función llamada por un programa principa que haga lo siguiente:

    1) Crear una matriz de 5 filas y 3 columnas.
    2) Cargar la tabla con: cadenas en la primera columna, calores enteros en la segunda columna, valores
    reales en la tercera columna. Estos datose se corresponden con numbre, edad y estatura de las personas
    que integran un equipo de vóley playa. Se asegurará de que los datos introducides sean correctos.
    3) Devolver la matriz cargada.

Diseñar una segunda función que, partiendo de una matriz y un número de columna, devuelva la media de los
elementos de esa columna.

Construir un módulo con las dos funciones anteriores.

En el programa principal se llamará a las funciones antes definidas (e incluidas en el módulo) para imprimir
los resultados que devuelven. En primer lugar (en forma bidimensional) los datos que contiene la matriz y, en
segundo lugar, los promedios de cada una de las 2 columnas numéricas.
"""

from modulo_ejercicio1 import cargar_matriz, media_columna

if __name__ == "__main__":
    matriz = cargar_matriz()
    print(matriz)
    print("Media de la columna 1:", media_columna(matriz, 1))
    print("Media de la columna 2:", media_columna(matriz, 2))