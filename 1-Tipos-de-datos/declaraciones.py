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
lista_iterable = [1,2,3]
for nombre_item in lista_iterable:
    # Chequear números pares
    if nombre_item % 2 == 0:
        print(nombre_item)
    else:
        print(f'Numero Impar:{nombre_item}')

lista_iterable = [1, 2, 3, 4,5,6,7, 8]
suma_lista = 0
for nombre_item in lista_iterable:
    suma_lista = suma_lista + nombre_item
    print(suma_lista)