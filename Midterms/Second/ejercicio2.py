"""Haga un programa que cree una interfaz gráfica (IGU) de la siguiente manera:

Se leerá un dato de "voltaje" en una entrada, otro de "resistencia" en otra entrada y otro de "corriente", 
dependiendo el botón que pulse el usuario se realizará el cálculo del dato faltante, que se visualizará 
en su lugar correspondiente.

El proceso deberá tener los botones de cálculo y uno de finalización del proceso.

El formato de la ventana así como los colores, tamaños etc. son libres.
"""

import tkinter as tk

def calcular_corriente():
    resultado = voltaje.get() / resistencia.get()
    corriente.set(resultado)

def calcular_resistencia():
    resultado = voltaje.get() / corriente.get()
    resistencia.set(resultado)

def calcular_voltaje():
    resultado = resistencia.get() * corriente.get()
    voltaje.set(resultado)

def finalizar():
    ventana.destroy()

# Define the main window
ventana = tk.Tk()
ventana.title('Segundo examen parcial')
ventana.geometry('500x200')

# Define the label and its position on the grid
etiqueta_titulo = tk.Label(ventana, text = 'Cálculo eléctrico')
etiqueta_titulo.grid(row=0, column=1, columnspan=2)

# Define the variables, labels and gird
voltaje = tk.DoubleVar()
voltaje.set('') # Set to blank
etiqueta_voltaje = tk.Label(ventana, text='Voltaje')
etiqueta_voltaje.grid(row=1, column=0)
entrada_voltaje = tk.Entry(ventana, textvariable=voltaje)
entrada_voltaje.grid(row=1, column=1)

resistencia = tk.DoubleVar()
resistencia.set('') # Set to blank
etiqueta_resistencia = tk.Label(ventana, text='Resistencia')
etiqueta_resistencia.grid(row=2, column=0)
entrada_resistencia = tk.Entry(ventana, textvariable=resistencia)
entrada_resistencia.grid(row=2, column=1)

corriente = tk.DoubleVar()
corriente.set('') # Set to blank
etiqueta_corriente = tk.Label(ventana, text='Corriente')
etiqueta_corriente.grid(row=3, column=0)
entrada_corriente = tk.Entry(ventana, textvariable=corriente)
entrada_corriente.grid(row=3, column=1)

# Definir botones de calculo
boton_calcular_corriente = tk.Button(ventana, text='Calcular corriente', command=calcular_corriente)
boton_calcular_corriente.grid(row=1, column=5)

boton_calcular_resistencia = tk.Button(ventana, text='Calcular resistencia', command=calcular_resistencia)
boton_calcular_resistencia.grid(row=2, column=5)

boton_calcular_voltaje =tk.Button(ventana, text='Calcular voltaje', command=calcular_voltaje)
boton_calcular_voltaje.grid(row=3, column=5)

# Definir boton de finalizacion de proceso
boton_finalizar = tk.Button(ventana, text='Finalizar', command=finalizar)
boton_finalizar.grid(row=4, column=6)

# Define main loop
ventana.mainloop()