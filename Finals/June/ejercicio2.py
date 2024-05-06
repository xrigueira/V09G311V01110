"""Diseñar un programa que se ejecute en un entorno gráfico similar al de la imagen1.jpeg

El usuario podrá introducir un radio cualquiera y elegir si quiere visualizar el diámetro de la
circumferencia, su longitud o la superficie del círculo.

Por defecto, la operación seleccionada es la de la obtención del diámetro, pero el usuario podrá
elegir la operación que desee.

Una vez se pulse el botón de "Ver resultado", se visualizará el resultado correspondiente a la
operación elegida y el radio introducido en la etiqueta habilitada a tal fin y colocada bajo el
botón.

Si el usuario teclea un radio inválido debe presentarse un menssaje de error indicativo en la
etiqueta habilitada para visualizar el resultado.
"""

# At least 45 min to write it and 30 to type it. AT LEAST.

import math
import tkinter as tk

def calcular():
    if var.get() == 'diametro':
        etiqueta_resultado.config(text = radio.get()*2)

    elif var.get() == 'circumferencia':
        etiqueta_resultado.config(text = 2 * math.pi * radio.get())

    elif var.get() == 'superficie':
        etiqueta_resultado.config(text = math.pi * pow(radio.get(), 2))

# Definir función para cerrar la ventana
def finalizar():
    ventana.destroy()

# Crear la ventana, su geometría y título
ventana = tk.Tk()
ventana.geometry('600x300')
ventana.title('ÁLGEBRA: CÍRCULOS Y CIRCUMFERENCIAS')

# Definir etiqueta radio
etiqueta_radio = tk.Label(ventana, text='Radio')
etiqueta_radio.grid(row=0, column=0)

# Definir entrada radio
radio = tk.IntVar()
radio.set('')
entrada_radio = tk.Entry(ventana, textvariable=radio)
entrada_radio.grid(row=0, column=1)

# Definir botón resultado y su etiqueta
boton_resultado = tk.Button(ventana, text='Ver resultado', command=calcular)
boton_resultado.grid(row=0, column=3)
etiqueta_resultado = tk.Label(ventana, text='Aquí visualizarás el resultado')
etiqueta_resultado.grid(row=1, column=3)

# Definir marco y radio buttons
marco = tk.LabelFrame(ventana, text='Selecciona operación')
marco.grid(row=3, column=2, columnspan=2)

var = tk.StringVar()
radio_1 = tk.Radiobutton(marco, text='Obtener diámetro', variable=var, value='diametro')
radio_1.select()
radio_1.grid(row=0, column=0)
radio_2 = tk.Radiobutton(marco, text='Obtener longitud de circumferencia', variable=var, value='circumferencia')
radio_2.grid(row=1, column=0)
radio_3 = tk.Radiobutton(marco, text='Calcular superficie círculo', variable=var, value='superficie')
radio_3.grid(row=2, column=0)

# Definir botón finalizar
boton_finalizar = tk.Button(ventana, text='Finalizar', command=finalizar)
boton_finalizar.grid(row=3, column=4)

# Definir el bucle principal
ventana.mainloop()