# condicionales
if True:
    print(True)

hambre = True
sed = True

if hambre and not sed:
    print('Tenemos hambre')
elif hambre == True and sed == True:
    print('Tenemos hambre y sed')
else:
    print('Estamops llenos')

# Iteraciones
lista_iterable = [1, 2, 3]
for nombre_item in lista_iterable:
    # Chequear números pares
    if nombre_item % 2 == 0:
        print(nombre_item)
    else:
        print(f'Numero Impar:{nombre_item}')

lista_iterable = [1, 2, 3, 4, 5, 6, 7, 8]
suma_lista = 0
for item in lista_iterable:
    suma_lista = suma_lista + item
    print(suma_lista)

for item in lista_iterable:
    # Chequera por números pares
    if item % 2 == 0:
        print(item)
    else:
        print(f'Número Impar:{item}')

for letter in 'Hola Mundo':
    print(letter)

mi_lista = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(mi_lista))
for item in mi_lista:
    print(item)

# Desempaquetando tuplas en una lista
for (a, b) in mi_lista:
    print(a)
    print(b)

d = {'y1': 1, 'y2': 2, 'y3': 3}
for llave, valor in d.items():
    print(llave)

