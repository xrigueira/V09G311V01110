"""
Definir un programe en Python cree una interfáz gráfica de cálculo de montante total para 
productos en un almacén. La aplicación debe permitir al usuario ingresar el código del producto, 
el nombre del producto, el precio individual y la cantidad en almacén. 

Luego, debe calcular el montante total multiplicando el precio individual por la cantidad en almacén.
Si el montante total es mayor o igual a 1000, se debe mostrar un mensaje indicando que se debe 
provisionar caja. 

Finalmente, se debe proporcionar un botón para cerrar la ventana.
"""

from tkinter import *

# Definir función para cerrar la ventana
def finalizar():
    ventana.destroy()

# Definir función para realiar el cálculo
def operar():
    mensaje.set("") # Limpiar el mensaje
    
    CP = codigo_producto.get() # Capturar los datos
    NP = nombre_producto.get()
    P = precio.get()
    C = cantidad.get()
    
    total = P * C # Operación principal
    
    if total >= 1000.0:  # Verificar la condición
        montante.set(total) # Visualizar el montante en su posición
        mensaje.set("Provisionar caja") # Visualizar la provisión
        mensaje_entrada.focus()
    else:
        montante.set(total) # Visualizar montante

# Crear la ventana, su geometría y título
ventana = Tk()
ventana.geometry('600x300')
ventana.title('Examen Final NO continua')

# Defininr el botón que llama a la función para borrar la ventana
boton_finalizar = Button(ventana, text ='Finalizar', command = finalizar)
boton_finalizar.grid(row=8, column= 1)

# Definir el botón que arranca el proceso de cálculo
boton_calcular = Button(ventana, text='Cálculo', command = operar)
boton_calcular.grid(row=6, column=2)

# Deinifir una etiqueta, una variable de entrada de código del producto y su cuadro de entrada
etiqueta_codigo_producto= Label(ventana, text= 'Código de Producto')
etiqueta_codigo_producto.grid(row=0, column=0)
codigo_producto = StringVar()
entrada_codigo_producto = Entry(ventana, textvariable = codigo_producto)
entrada_codigo_producto.grid(row=0, column=1)

# Definit una etiqueta, una variable de entrada del nombre del producto y su cuadro de entrada 
etiqueta_nombre_producto = Label(ventana, text='Nombre del producto')
etiqueta_nombre_producto.grid(row=1, column=0)
nombre_producto = StringVar() 
entrada_nombre_producto = Entry(ventana, textvariable = nombre_producto)
entrada_nombre_producto.grid(row=1, column=1)

# Definir una etiqueta, una variable de entrada del precio individual y su cuadro de entrada
etiqueta_precio = Label(ventana, text='Precio individual')
etiqueta_precio.grid(row=2, column=0)
precio = DoubleVar() 
entrada_precio = Entry(ventana, textvariable = precio)
entrada_precio.grid(row=2, column=1)

# Definir una etiqueta, una variable de entrada de la cantidad en almacén y su cuadro de entrada
etiquetaCantidad = Label(ventana, text='Cantidad en almacén')
etiquetaCantidad.grid(row=3, column=0)
cantidad= IntVar() 
entradaCantidad = Entry(ventana, textvariable = cantidad)
entradaCantidad.grid(row=3, column=1)

# Definir una etiqueta de montante, una variable de montante y su cuadro de salida
etiquetaMontante = Label(ventana, text= 'Montante Total')
etiquetaMontante.grid(row=4,column=0)
montante = DoubleVar() 
salidaMontante = Entry(ventana, textvariable = montante, state = "readonly")
salidaMontante.grid(row=4,column=1)

# Definir una variable de mensaje y su cuadro de salida 
mensaje = StringVar() 
mensaje_entrada = Entry(ventana, textvariable = mensaje, state = "readonly")
mensaje_entrada.grid(row=5,column=1)

#Inicio la ventana
ventana.mainloop()
