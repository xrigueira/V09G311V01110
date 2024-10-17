"""
Reproducir la interfaz gráfica que se muestra en las imágenes. Al pulsar el botón de cálculo, 
se multiplicarán los 2 valores dados por el usuario y se visualizará el resultado como aparece en la figura a.
Si el usuario teclea valores erróneos, se visualizará el resultado como aparece en la figura b.
"""

import tkinter as tk
from tkinter import messagebox


def calculo():
    try:
        valor_1 = float(valor_1_entry.get())
        valor_2 = float(valor_2_entry.get())
        resultado = valor_1 * valor_2
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")

ventana = tk.Tk()
ventana.title("Examen Xullo exercicio 3")
ventana.geometry("600x200")

valor_1_label = tk.Label(ventana, text="Valor 1:")
valor_1_label.grid(row=0, column=0)

valor_1_entry = tk.Entry(ventana)
valor_1_entry.grid(row=0, column=1)

valor_2_label = tk.Label(ventana, text="Valor 2:")
valor_2_label.grid(row=1, column=0)

valor_2_entry = tk.Entry(ventana)
valor_2_entry.grid(row=1, column=1)

calcular_button = tk.Button(ventana, text="Calcular", command=calculo)
calcular_button.grid(row=3, column=3)

resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.grid(row=3, column=1)

fin_button = tk.Button(ventana, text="Finalizar", command=ventana.destroy)
fin_button.grid(row=4, column=1)

ventana.mainloop()
