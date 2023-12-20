# import

# condicionales
if True:
    print(True)

hambre = True
sed = True

if hambre and not sed:
    print('Tenemos hambre')
elif hambre is True and sed is True:
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

x = 0
while x < 5:
    print(f'El valor actual de x es {x}')
    x += 1
else:
    print('x no es mayor que 5')

# Palabras Claves Utiles
# breack
# continue
# pass

x = 'Erick'

for letter in x:
    if letter == 'i':
        break
        # continue
    print(letter)

milista = [1, 2, 3]
for num in range(0, 10, 2):
    print(num)

print(list(range(0, 11, 2)))

palabra = 'hola'
for index, letter in enumerate(palabra):
    print(index)
    print(letter)
    print('\n')

milista1 = [1, 2, 3, 4, 5]
milista2 = ['a', 'b', 'c']
milista3 = [100, 200, 300]

for item in zip(milista1, milista2, milista3):
    print(item)

print(list(zip(milista1, milista2, milista3)))

if 'a' in milista2:
    print('verdadero')

d = {'k1': 1}
if 'k1' in d:
    print('verdadero')

print(min(milista1))
