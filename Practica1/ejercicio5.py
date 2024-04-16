"""
Escribe un programa que lea el nombre y el apellido de una persona y obtenga (y
visualice) su correo electrónico, teniendo en cuenta que el nombre de usuario se obtiene
como la inicial del nombre, seguida del apellido más @alumnos.uvigo.es.
"""

nombre = 'Xurxo'
apellido = 'Rigueira'

correo = nombre[0].lower() + apellido.lower() + '@alumnos.uvigo.es'

print(correo)