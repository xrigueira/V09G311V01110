def cargar_matriz():
    matriz = []
    for i in range(5):
        fila = []
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        estatura = float(input("Ingrese la estatura de la persona: "))
        fila.append(nombre)
        fila.append(edad)
        fila.append(estatura)
        matriz.append(fila)
    return matriz

def media_columna(matriz, columna):
    suma = 0
    for fila in matriz:
        suma += int(fila[columna])
    return suma / len(matriz)