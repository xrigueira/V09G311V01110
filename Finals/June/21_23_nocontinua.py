#Examen Final EEM parte IGU
#autor: Prof. Dr. Manuel Pérez Cota
#20210611v; mod 20230531 sin locale

from tkinter import *

#Función para borrar la pantalla (quitar la ventana)
def Salir():
    xanela.destroy()

#Función para iniciar el cálculo
def Calcula():
    Mensaxe.set("") #limpio mensaje
    CP = CodProd.get() #campuro datos
    NP = NomProd.get()
    P = Precio.get()
    C = Cantidad.get()
    total = P * C
    if total >= 100000.0:  #checo la condición
        Montante.set(total) #visualizo el montante en su posición
        Mensaxe.set("Provisionar caja") #visualizo la provisión
        salidaMensaxe.focus()
    else:
        Montante.set(total) #visualizo montante

#Crear la ventana, su geometría y título
xanela = Tk()
xanela.geometry('600x300')
xanela.title('Examen Final NO continua')

#Creo el botón que llama a la función para borrar la ventana
botonSalir = Button(xanela, text ='FIN', command = Salir)
botonSalir.grid(row=8, column= 1)

#Creo el botón que arranca el proceso de cálculo
botonarranque = Button(xanela,text='Cálculo', command = Calcula)
botonarranque.grid(row=6, column=2)

#Creo una etiqueta, una variable de entrada de código del producto y su cuadro de entrada
etiquetaCodProd= Label(xanela,text= 'Código de Producto')
etiquetaCodProd.grid(row=0,column=0)
CodProd = StringVar() 
entradaCodProd = Entry(xanela, textvariable = CodProd)
entradaCodProd.grid(row=0,column=1)

#Creo una etiqueta, una variable de entrada del nombre del producto y su cuadro de entrada 
etiquetaNomProd = Label(xanela,text='Nombre del producto')
etiquetaNomProd.grid(row=1,column=0)
NomProd = StringVar() 
entradaNomProd = Entry(xanela, textvariable = NomProd)
entradaNomProd.grid(row=1,column=1)

#Creo una etiqueta, una variable de entrada del precio individual y su cuadro de entrada
etiquetaPrecio = Label(xanela,text='Precio individual')
etiquetaPrecio.grid(row=2,column=0)
Precio = DoubleVar() 
entradaPrecio = Entry(xanela, textvariable = Precio)
entradaPrecio.grid(row=2,column=1)

#Creo una etiqueta, una variable de entrada de la cantidad en almacén y su cuadro de entrada
etiquetaCantidad = Label(xanela,text='Cantidad en almacén')
etiquetaCantidad.grid(row=3,column=0)
Cantidad= IntVar() 
entradaCantidad = Entry(xanela, textvariable = Cantidad)
entradaCantidad.grid(row=3,column=1)

#Creo una etiqueta de montante, una variable de montante y su cuadro de salida
etiquetaMontante = Label(xanela,text= 'Montante Total')
etiquetaMontante.grid(row=4,column=0)
Montante = DoubleVar() 
salidaMontante = Entry(xanela, textvariable = Montante, state = "readonly")
salidaMontante.grid(row=4,column=1)

#Creo una variable de mensaje y su cuadro de salida 
Mensaxe = StringVar() 
salidaMensaxe = Entry(xanela, textvariable = Mensaxe, state = "readonly")
salidaMensaxe.grid(row=5,column=1)

#Inicio la ventana
xanela.mainloop()
