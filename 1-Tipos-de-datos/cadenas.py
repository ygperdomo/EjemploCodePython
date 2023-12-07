print("Hola \nmundo")

print(len("hola"))

micadena = "hola mundo"
print(micadena[3])
print(micadena[-1])  # Indexado inverso
print(micadena[0:7:2])

name = "Pam"
ultimas_letras = name[1:]
print('p' + ultimas_letras)

letra = 'z'
letra = letra * 10
print(letra)

x = 'hola mundo'
x = x.upper()
print(x)

x = x.split('O')
print(x)

# interpolación de cadena
print('Esto {} una {} de {}'.format('es', 'cadena', 'TEXTO'))
print('Esto {e} una {c} de {t}'.format(e='es', c='cadena', t='TEXTO'))

resultados = 100 / 888
# formateo de float "{valor: width.precicision f}"
print("Los resultados son {r:1.5f}".format(r=resultados))

nombre = "Erick"
edad = 36
print(f"Los resultados son {nombre} con edad de {edad}")

# Listas
mi_lista = ['cadena', 2, 3]
otra_lista = ['cuatro', 'cinco']

print(mi_lista)
print(len(mi_lista))
print(mi_lista[0])
print(mi_lista[1:])
print(mi_lista + otra_lista)

nueva_lista = mi_lista + otra_lista
nueva_lista.append('seis')
print(nueva_lista)
item_popeado = nueva_lista.pop()
print(nueva_lista)
item_popeado = nueva_lista.pop(2)
print(nueva_lista)
print(item_popeado)

mi_lista = ['a', 'z', 'x', 'b', 'd']
num_lista = [4, 1, 5, 7, 3]

mi_lista.sort()
print(mi_lista)
mi_lista.reverse()
print(mi_lista)

# Diccionarios
mi_diccionario = {'manzanas': '2.90', 'agua': '3.25', 'kekes': ['manzana', 'platano']}
print(mi_diccionario)
print(mi_diccionario['manzanas'])
print(mi_diccionario['kekes'])
print(mi_diccionario['kekes'][1].upper())

mi_diccionario['gaseosa'] = 300
print(mi_diccionario)
print(mi_diccionario.keys())
print(mi_diccionario.values())
print(mi_diccionario.items())

# tuplas
t = (1, 2, 3)
lista = [1, 2, 3]

print(type(t))
print(t[0])

t = ('a', 'b', 'a')
print(t.count('a'))

t = ('c', 'b', 'a')
print(t.index('a'))

lista[0] = 'nuevo'
print(lista)

