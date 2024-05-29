"""
Diseñar una interfaz gráfica que permita calcular la distancia entre dos puntos y el punto medio de estos.

Comentarios en relación a la interfaz gráfica:
    El usuario podrá introducir las coordenadas de los dos puntos y elegir si quiere visualizar su distancia o el punto medio entre ambos.
    Por defecto, la operación seleccionada es la del cálculo de la distancia, pero el usuario podrá elegir la operación que desee.
    Una vez se pulse el botón de “Obtener resultado”, se visualizará el resultado correspondiente a la operación elegida y los puntos introducidos en la etiqueta habilitada a tal fin y colocada bajo el botón.
    En caso de error en la introducción de las coordenadas, se presentará un mensaje de error al usuario.
    Habrá un botón que permita el borrado de las coordenadas introducidas y otro para finalizar el programa.

Comentarios en relación al programa:
    1. Se definirá una función que, partiendo de dos datos numéricos, devuelva una tupla integrada por ambos.
    2. Se definirá una función que, partiendo de dos puntos (dos tuplas) devuelva la distancia entre ambos.
    3. Se definirá una función que, partiendo de dos puntos (dos tuplas) devuelva, en otra tupla, el punto medio.
    4. Se llamará a estas funciones para presentar al usuario los resultados que solicite.
"""

import tkinter as tk

# Define function that takes coordinates and returns a tuple
def coor2tuple(x, y):
    return (x, y)

def finalizar():
    ventana.destroy()

# Define function to calculate the distance
def calcular_distancia(tupla1, tupla2):
    resultado = ((tupla2[0] - tupla1[0])**2 + (tupla2[1] - tupla1[1])**2)**0.5
    return resultado

# Define function to calculate the midpoint
def calcular_punto_medio(tupla1, tupla2):
    resultado_x = (tupla1[0] + tupla2[0])/2
    resultado_y = (tupla1[1] + tupla2[1])/2
    return (resultado_x, resultado_y)

def calcular():
    
    if opcion_calculo.get() == 0:
        tupla1 = coor2tuple(x1.get(), y1.get())
        tupla2 = coor2tuple(x2.get(), y2.get())
        resultado = calcular_punto_medio(tupla1=tupla1, tupla2= tupla2)
        etiqueta_resultado.config(text=f'El punto medio es ({resultado[0]}, {resultado[1]})')
    
    elif opcion_calculo.get() == 1:
        tupla1 = coor2tuple(x1.get(), y1.get())
        tupla2 = coor2tuple(x2.get(), y2.get())
        resultado = calcular_distancia(tupla1=tupla1, tupla2=tupla2)
        etiqueta_resultado.config(text=f'La distancia entre los puntos {resultado}')

def borrar():
    x1.set('')
    y1.set('')
    x2.set('')
    y2.set('')

# Define the main window
ventana = tk.Tk()
ventana.title('Cálculos con puntos')
ventana.geometry('900x200')

# Define frame
marco = tk.LabelFrame(ventana, text='INTRODUCCIÓN DE COORDENADAS')
marco.grid(row=0, column=0)

# # Define the variables, labels and gird
etiqueta_primer_punto = tk.Label(marco, text='Primer punto')
etiqueta_primer_punto.grid(row=0, column=0)

etiqueta_segundo_punto = tk.Label(marco, text='Segundo punto')
etiqueta_segundo_punto.grid(row=1, column=0)

x1 = tk.DoubleVar()
x1.set('') # Set to blank
etiqueta_x1 = tk.Label(marco, text='Coordinada x')
etiqueta_x1.grid(row=0, column=1)
entrada_x1 = tk.Entry(marco, textvariable=x1)
entrada_x1.grid(row=0, column=2)

y1 = tk.DoubleVar()
y1.set('') # Set to blank
etiqueta_y1 = tk.Label(marco, text='Coordinada y')
etiqueta_y1.grid(row=0, column=3)
entrada_y1 = tk.Entry(marco, textvariable=y1)
entrada_y1.grid(row=0, column=4)

x2 = tk.DoubleVar()
x2.set('') # Set to blank
etiqueta_x2 = tk.Label(marco, text='Coordinada x')
etiqueta_x2.grid(row=1, column=1)
entrada_x2 = tk.Entry(marco, textvariable=x2)
entrada_x2.grid(row=1, column=2)

y2 = tk.DoubleVar()
y2.set('') # Set to blank
etiqueta_y2 = tk.Label(marco, text='Coordinada y')
etiqueta_y2.grid(row=1, column=3)
entrada_y2 = tk.Entry(marco, textvariable=y2)
entrada_y2.grid(row=1, column=4)

etiqueta_resultado = tk.Label(text='Aquí visualizarás el resultado')
etiqueta_resultado.grid(row=2, column=1)

# Define buttons
marco_radio = tk.LabelFrame(ventana, text='Elige una operación')
marco_radio.grid(row=1, column=0)

opcion_calculo = tk.IntVar()
radio_punto_medio = tk.Radiobutton(marco_radio, text='Cálculo del punto medio', variable=opcion_calculo, 
                                value=0)
radio_punto_medio.grid(row=0, column=0)
radio_punto_medio.select()

radio_distancia = tk.Radiobutton(marco_radio, text='Cálculo de la distancia', variable=opcion_calculo,
                                value=1)
radio_distancia.grid(row=1, column=0)

boton_resultado = tk.Button(ventana, text='Obtener resultado', command=calcular)
boton_resultado.grid(row=1, column=1)

boton_borrar = tk.Button(ventana, text='Borrar datos introducidos', command=borrar)
boton_borrar.grid(row=0, column=2)

boton_finalizar = tk.Button(ventana, text='Finalizar', command=finalizar)
boton_finalizar.grid(row=1, column=2)

# Define the main loop
ventana.mainloop()
