"""
Diseñar una ventana que ejecute un programa calculadora como el que se muestra en la imagen.

Ten en cuenta que:

Al seleccionar la operación deseada, se cambian las etiquetas de los números (primer sumando y segundo sumando; minuendo y sustraendo, primer factor y segundo factor; dividendo y divisor).
Al pulsar el botón "Calcular" visualizaremos el resultado correspondiente.
Al pulsar el botón "Finalizar", terminamos la ejecución del programa.
Al pulsar el botón "Borrar datos introducidos", se resetean los valores introducidos dejando los cuadros de entrada en blanco
"""

import tkinter as tk

def calcular():
    if operacion.get() == "+":
        resultado.set(int(num1.get()) + int(num2.get()))
    elif operacion.get() == "-":
        resultado.set(int(num1.get()) - int(num2.get()))
    elif operacion.get() == "*":
        resultado.set(int(num1.get()) * int(num2.get()))
    elif operacion.get() == "/":
        resultado.set(int(num1.get()) / int(num2.get()))

def borrar():
    num1.set("")
    num2.set("")
    resultado.set("")
    operacion.set("")

def finalizar():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x200")

num1 = tk.StringVar()
num2 = tk.StringVar()
resultado = tk.StringVar()
operacion = tk.StringVar()

etiqueta1 = tk.Label(ventana, text="Primer sumando")
etiqueta1.grid(row=0, column=0)
entrada1 = tk.Entry(ventana, textvariable=num1)
entrada1.grid(row=0, column=1)

etiqueta2 = tk.Label(ventana, text="Segundo sumando")
etiqueta2.grid(row=1, column=0)
entrada2 = tk.Entry(ventana, textvariable=num2)
entrada2.grid(row=1, column=1)

etiqueta3 = tk.Label(ventana, text="Resultado")
etiqueta3.grid(row=2, column=0)
entrada3 = tk.Entry(ventana, textvariable=resultado)
entrada3.grid(row=2, column=1)

etiqueta4 = tk.Label(ventana, text="Operación")
etiqueta4.grid(row=3, column=0)
entrada4 = tk.Entry(ventana, textvariable=operacion)
entrada4.grid(row=3, column=1)

boton1 = tk.Button(ventana, text="Calcular", command=calcular)
boton1.grid(row=4, column=0)

boton2 = tk.Button(ventana, text="Borrar datos introducidos", command=borrar)
boton2.grid(row=4, column=1)

boton3 = tk.Button(ventana, text="Finalizar", command=finalizar)
boton3.grid(row=4, column=2)

ventana.mainloop()