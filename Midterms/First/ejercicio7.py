
"""Itachi Uchiha tiene el Mangekyo Sharingan, este es un jutsu visual muy poderoso, 
pero solo lo puede utilizar 10 veces. Al llegar a la décima vez se quedará ciego. 
Queremos ayudar a que Itachi use el Mangekyo Sharingan con cabeza. Construye dos programas, 
con conceptos distintos y uno de ellos utilizando listas, que lleven la cuenta de cuantas 
veces Itachi ha utilizado en Mangekyo Sharingan y que le avise a la novena vez de que a la 
siguiente perderá la vista.
"""

#%% Opcion 1
# Inicializamos el contador de usos del Mangekyo Sharingan a 0
usos_mangekyo_sharingan = 0

# Simulamos el uso del Mangekyo Sharingan 10 veces
for _ in range(10):
    usos_mangekyo_sharingan += 1
    print(f'Itachi ha usado el Mangekyo Sharingan {usos_mangekyo_sharingan} veces')

    # Si Itachi ha usado el Mangekyo Sharingan 9 veces le avisamos
    if usos_mangekyo_sharingan == 9:
        print('Itachi, te queda un uso del Mangekyo Sharingan antes de perder la vista')
    
# Si Itachi ha usado el Mangekyo Sharingan 10 veces, le informamos que ha pedido la vista
if usos_mangekyo_sharingan == 10:
    print('Itachi ha perdido la vista por el uso excesivo del Mangekyo Sharingan')

#%% Opcion 2
# Inicializamos el contador de usos del Mangekyo Sharingan a 0
usos_mangekyo_sharingan = 0

# Simulamos el uso del Mangekyo Sharingan 10 veces
while usos_mangekyo_sharingan < 10:
    usos_mangekyo_sharingan += 1
    print(f'Itachi ha usado el Mangekyo Sharingan {usos_mangekyo_sharingan} veces')

    # Si Itachi ha usado el Mangekyo Sharingan 9 veces le avisamos
    if usos_mangekyo_sharingan == 9:
        print('Itachi, te queda un uso del Mangekyo Sharingan antes de perder la vista')
    
if usos_mangekyo_sharingan == 10:
    print('Itachi ha perdido la vista por el uso excesivo del Mangekyo Sharingan')

#%% Opcion 3
# Lista para almacenar los usos del Mangekyo Sharingan
usos_mangekyo_sharingan = []

# Simulamos el uso del Mangekyo Sharingan 10 veces
while len(usos_mangekyo_sharingan) < 10:
    # Agregar un elemento a la lista
    usos_mangekyo_sharingan.append(None)
    print(f'Itachi ha usado el Mangekyo Sharingan {len(usos_mangekyo_sharingan)} veces')

    # Si Itachi ha usado el Mangekyo Sharingan 9 veces le avisamos
    if len(usos_mangekyo_sharingan) == 9:
        print('Itachi, te queda un uso del Mangekyo Sharingan antes de perder la vista')

# Mensaje final
print('Itachi ha perdido la vista por el uso excesivo del Mangekyo Sharingan')
