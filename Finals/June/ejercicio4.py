"""
Diseñe un programa en el cual el usuario pueda dar un texto y este aparezca como un letrero.
Deberá utilizar al menos una instrucción de ciclo.
(ver el ejemplo de la ejecución a continuación):
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | r | o | g | r | a | m | a |   | d | e |   | e | x | a | m | e | n |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
"""

texto = input("Ingrese un texto: ")
print("+---" * len(texto) + "+")
for letra in texto:
    print("| " + letra + " ", end="")
print("|")
print("+---" * len(texto) + "+")
