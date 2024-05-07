import math as m
import tkinter as tk

def calcular_faltante():

    if (hipotenusa.get() != 0) and (cateto_1.get() != 0):
        cateto_2.set(m.sqrt(pow(hipotenusa.get(), 2) - pow(cateto_1.get(), 2)))

    elif (hipotenusa.get() != 0) and (cateto_2.get() != 0):
        cateto_1.set(m.sqrt(pow(hipotenusa.get(), 2) - pow(cateto_2.get(), 2)))

    elif (cateto_1.get() != 0) and (cateto_2.get() != 0):
        hipotenusa.set(m.sqrt(pow(cateto_1.get(), 2) + pow(cateto_2.get(), 2)))
    
    else:
        print('Faltan datos para calcular el faltante')

def perimetro():
    resultado = hipotenusa.get() + cateto_1.get() + cateto_2.get()
    etiqueta_perimetro.config(text=resultado)

def area():
    resultado = 0.5 * cateto_1.get() * cateto_2.get()
    etiqueta_area.config(text=resultado)

# Definir ventana
ventana = tk.Tk()
ventana.geometry("400x200")
ventana.title("Triangulos rectángulos")

# Definir etiquetas
etiqueta_cateto_1 = tk.Label(ventana, text='Cateto 1')
etiqueta_cateto_1.grid(row=0, column=0)
etiqueta_cateto_2 = tk.Label(ventana, text='Cateto 2')
etiqueta_cateto_2.grid(row=1, column=0)
hipotenusa = tk.Label(ventana, text='Hipotenusa')
hipotenusa.grid(row=2, column=0)

# Definir entradas
cateto_1 = tk.DoubleVar()
cateto_1.set(0)
entrada_cateto_1 = tk.Entry(ventana, textvariable=cateto_1)
entrada_cateto_1.grid(row=0, column=1)
cateto_2 = tk.DoubleVar()
cateto_2.set(0)
entrada_cateto_2 = tk.Entry(ventana, textvariable=cateto_2)
entrada_cateto_2.grid(row=1, column=1)
hipotenusa = tk.DoubleVar()
hipotenusa.set(0)
entrada_hipotenusa = tk.Entry(ventana, textvariable=hipotenusa)
entrada_hipotenusa.grid(row=2, column=1)

# Definir botones
boton_calculo_faltante = tk.Button(ventana, text='Calcular faltante', command=calcular_faltante)
boton_calculo_faltante.grid(row=0, column=3)

boton_calculo_perimetro = tk.Button(ventana, text='Perímetro', command=perimetro)
boton_calculo_perimetro.grid(row=4, column=2)
boton_calculo_area = tk.Button(ventana, text='Área', command=area)
boton_calculo_area.grid(row=5, column=2)

# Definir etiqueta resultado
etiqueta_perimetro = tk.Label(ventana, text='Aquí puedes ver el perímetro')
etiqueta_perimetro.grid(row=4, column=1)
etiqueta_area = tk.Label(ventana, text='Aquí puedes ver el área')
etiqueta_area.grid(row=5, column=1)

# Definir el bucle principal
ventana.mainloop()
