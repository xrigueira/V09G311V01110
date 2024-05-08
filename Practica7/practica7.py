"""
Diseñar una ventana que ejecute un programa calculadora como el que se muestra en la imagen.

Ten en cuenta que:

Al seleccionar la operación deseada, se cambian las etiquetas de los números (primer sumando y segundo sumando; minuendo y sustraendo, primer factor y segundo factor; dividendo y divisor).
Al pulsar el botón "Calcular" visualizaremos el resultado correspondiente.
Al pulsar el botón "Finalizar", terminamos la ejecución del programa.
Al pulsar el botón "Borrar datos introducidos", se resetean los valores introducidos dejando los cuadros de entrada en blanco
"""

import tkinter as tk 

def etiquetas():
    if var.get() == 1:
        etiqueta_num1.config(text = 'Primer sumando')
        etiqueta_num2.config(text = 'Segundo sumando')
    
    elif var.get() == 2:
        etiqueta_num1.config(text = 'Minuendo')
        etiqueta_num2.config(text = 'Sustraendo')
    
    elif var.get() == 3:
        etiqueta_num1.config(text = 'Primer factor')
        etiqueta_num2.config(text = 'Segundo factor')
    
    elif var.get() == 4:
        etiqueta_num1.config(text = 'Dividendo')
        etiqueta_num2.config(text = 'Divisor')

def operar():

    try:
        num1_val = num1.get()
        num2_val = num2.get()
    except tk._tkinter.TclError:
        etiqueta_resultado.config(text = 'Introduce un número válido')
        return
    
    if var.get() == 1:
        result = num1.get() + num2.get()
    
    elif var.get() == 2:
        result = num1.get() - num2.get()
    
    elif var.get() == 3:
        result = num1.get() * num2.get()
    
    elif var.get() == 4:
        if num2.get() == 0:
            result = 'No se puede dividir entre 0'
        else:
            result = num1.get() / num2.get()

    etiqueta_resultado.config(text = result)

def borrar():
    num1.set('')
    num2.set('')
    etiqueta_resultado.config(text = 'Aquí visualizaremos el resultado')

def finalizar():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x200")

var = tk.IntVar()
result = tk.StringVar()

etiqueta_titulo = tk.Label(ventana, text = 'Operaciones con dos numeros')
etiqueta_titulo.grid(row=0, column=1, columnspan=3)

etiqueta_num1 = tk.Label(ventana, text = 'Primer sumando')
num1 = tk.DoubleVar()
num1.set('')
entrada_num1 = tk.Entry(ventana, textvariable=num1)
etiqueta_num1.grid(row=1, column=0)
entrada_num1.grid(row=1, column=1)

etiqueta_num2 = tk.Label(ventana, text = 'Segundo sumando')
num2 = tk.DoubleVar()
num2.set('')
entrada_num2 = tk.Entry(ventana, textvariable=num2)
etiqueta_num2.grid(row=2, column=0)
entrada_num2.grid(row=2, column=1)

marco_seleccion = tk.LabelFrame(ventana, text = 'Elige una operación')
marco_seleccion.grid(row=3, column=0, columnspan=2)
r1 = tk.Radiobutton(marco_seleccion, text = 'Suma', variable=var, value = 1, command=etiquetas)
r1.select()
r1.grid(row=0, column=0)
r2 = tk.Radiobutton(marco_seleccion, text = 'Resta', variable=var, value = 2, command=etiquetas)
r2.grid(row=0, column=1)
r3 = tk.Radiobutton(marco_seleccion, text = 'Multiplicación', variable=var, value = 3, command=etiquetas)
r3.grid(row=0, column=2)
r4 = tk.Radiobutton(marco_seleccion, text = 'División', variable=var, value = 4, command=etiquetas)
r4.grid(row=0, column=3)

# Definir botones
boton_calcular = tk.Button(ventana, text = 'Calcular', command=operar)
boton_calcular.grid(row=1, column=3)

etiqueta_resultado = tk.Label(ventana, text = 'Aquí visualizaremos el resultado')
etiqueta_resultado.grid(row=2, column=3)

boton_borrar = tk.Button(ventana, text = 'Borrar datos introducidos', command=borrar)
boton_borrar.grid(row=4, column=3)

boton_finalizar = tk.Button(ventana, text = 'Finalizar', command=finalizar)
boton_finalizar.grid(row=5, column=3)

ventana.mainloop()