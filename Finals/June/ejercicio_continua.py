import os

#Función de carga de datos
def cargadatos(nomefich):
    #abro o ficheiro para engadir datos
    ficheiro = open(nomefich,'a')
    #creo os datos que vou utilizar
    CodProd = ""
    NomProd = ""
    Precio = 0.0
    CantAlm = 0
    opc = input("Queres meter datos no ficheiro? ")
    while "N" != opc.upper():
        CodProd = str(input("Dame el código del producto: "))
        NomProd = str(input("Dame el nombre del producto: ")) 
        Precio = float(input("Dame el precio: "))
        CantAlm= int(input("Dame la cantidad en almacén: "))
        ficheiro.write(CodProd + "\r") #grabo os datos
        ficheiro.write(NomProd + "\r")
        ficheiro.write(str(Precio)+"\r")
        ficheiro.write(str(CantAlm) + "\r")
        opc = input("¿Quieres meter mas datos (N=no)? ")        
    ficheiro.close()

#Función de listado
def listado(nomefich):
    os.system("cls")
    print ("LISTADO")
    #abro o ficheiro para ler datos
    ficheiro = open(nomefich,'r')
    print ("Código"+"\t"+"Nombre"+ "\t"*2+ "Precio"+"\t"+"Cantidad")
    for lineaCod in ficheiro: #utilizo de pivote para ler e de control do ciclo o dato do nome
        lineaNom = ficheiro.readline()
        lineaPrecio = ficheiro.readline()
        lineaCant = ficheiro.readline()
        print(lineaCod[:-1]+"\t"+lineaNom[:-1]+"\t"*2+lineaPrecio[:-1]+"\t"+lineaCant) #o -1 e para quitar o salto de renglón
    #unha vez acabado pecho o ficheiro
    ficheiro.close()

#Función de modificar datos
def modifica(nomefich):
    os.system("cls")
    #abro o ficheiro para ler datos e outro para copiar
    ficheiro1 = open(nomefich,'r')
    ficheiro2 = open("copia.txt", 'w')
    for lineaCod in ficheiro1:
        lineaNom = ficheiro1.readline()
        lineaPrecio = ficheiro1.readline()
        lineaCant = ficheiro1.readline()
        os.system("cls")
        print("Código = {0} Nome = {1}".format(lineaCod[:-1],lineaNom[:-1]))
        print("Precio = {0} Cantidad = {1}".format(lineaPrecio[:-1],lineaCant[:-1]))
        cambio = str(input("¿Qué quieres cambiar el precio(p) o la cantidad en almacén (c) o nada(n)? " ))
        if cambio.lower() == "p":
            precio = float(input("Dame el Precio: "))
            if precio < 0.0 :
                Precioleido = float(lineaPrecio[:-1])
            else:
                Precioleido = precio
            lineaPrecio = str(Precioleido)+"\r"
        elif cambio.lower() == "c":
            cantidad = int(input("Dame la cantidad: "))
            if cantidad <= 0.0 :
                Cantidadleida = int(lineaCant[:-1])
            else:
                Cantidadleida = int(lineaCant[:-1]) + cantidad
            lineaCant = str(Cantidadleida)+"\r"
        elif cambio.lower() == "n":
            print ("Sin cambios ")            
        print(" ")
        ficheiro2.write(lineaCod)
        ficheiro2.write(lineaNom)
        ficheiro2.write(lineaPrecio)
        ficheiro2.write(lineaCant)
    #unha vez acabado pecho os ficheiros
    ficheiro1.close()
    ficheiro2.close()
    #fago a copia do ficheiro copia.txt no ficheiro principal
    os.remove(nomefich)
    os.rename('copia.txt',nomefich)

#Creo, se non existe, o ficheiro co que se vai traballar
def creafich():
    nomefich = str(input("Dime o nome do ficheiro coa ruta "))
    existe = os.path.isfile(nomefich)
    if existe == False:
        ficheiro = open(nomefich,'w') #si no existe lo creo
        ficheiro.close() #pechoo sempre porque abrirase dependendo da opción
    return nomefich

#menu principal
def menu():
    ficheiro = ""
    ficheiro = creafich()
    opcion = ""
    while opcion.upper() != "F":
        os.system("cls")
        print("Menú")
        print("\tC)Cargar nuevos datos en el fichero")
        print("\tM)Modificar alguno de los datos del fichero (solo precio y cantidad)")
        print("\tL)Listar todos los elementos dle fichero")
        print("\tF)FIN")
        opcion = input("\nOpción: ")
        if opcion.upper() == "C":
            cargadatos(ficheiro)
        elif opcion.upper() == "M":
            modifica(ficheiro)
        elif opcion.upper() == "L":
            listado(ficheiro)
        elif opcion.upper() == "F":
            print ("Fin de programa")
        else : print("opción non válida")

#Programa principal
menu()
