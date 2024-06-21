"""
Se desea diseñar una Interfaz gráfica como la que se muestra en la imagen y en la que se puedan introducir los siguientes datos:
- Nombre del producto: Se selecciona en un combobox entre los materiales almacenados
- Precio individual: tipo real
- Cantidad en almacén: tipo entero

Además:
- La ventana dispondrá de un botón para finalizar el programa.
- La ventana dispondrá también de un botón para borrar los datos introducidos.
- Por último, la ventana dispondrá de un botón de cálculo que obtendrá el valor total del producto 
almacenado (Valor total = Precio individual * Cantidad en almacén) y lo visualizará en la etiqueta habilitada a tal fin.
"""

import tkinter as tk

def calcular():
	precio = float(precio_entry.get())
	cantidad = int(cantidad_entry.get())
	total = precio * cantidad
	total_label.config(text=f"Total: {total}")

def borrar():
	nombre_combobox.set("")
	precio_entry.delete(0, tk.END)
	cantidad_entry.delete(0, tk.END)
	total_label.config(text="Total: ")

def finalizar():
	ventana.destroy()

ventana = tk.Tk()
ventana.title("PRODUCTOS EN ALMACÉN")
ventana.geometry("600x200")

marco = tk.LabelFrame(ventana, text="DATOS SOBRE EXISTENCIAS")
grid = marco.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
nombre_label = tk.Label(marco, text="Nombre del producto")
nombre_label.grid(row=0, column=0)

nombre_combobox = tk.StringVar()
nombre_combobox.set("")
menu_combobox = tk.OptionMenu(marco, nombre_combobox, "Oro", "Plata", "Boro")
menu_combobox.grid(row=1, column=0)

precio_label = tk.Label(marco, text="Precio unitario:")
precio_label.grid(row=0, column=1)

precio_entry = tk.Entry(marco)
precio_entry.grid(row=0, column=2)

cantidad_label = tk.Label(marco, text="Cantidad en almacén")
cantidad_label.grid(row=1, column=1)

cantidad_entry = tk.Entry(marco)
cantidad_entry.grid(row=1, column=2)

calcular_button = tk.Button(ventana, text="Obtener el valor del producto almacenado", command=calcular)
calcular_button.grid(row=3, column=0)

borrar_button = tk.Button(ventana, text="Borrar", command=borrar)
borrar_button.grid(row=0, column=3)

total_label = tk.Label(ventana, text="Aquí visualizarás el resultado")
total_label.grid(row=4, column=0)

finalizar_button = tk.Button(ventana, text="Finalizar", command=finalizar)
finalizar_button.grid(row=3, column=3)

ventana.mainloop()

