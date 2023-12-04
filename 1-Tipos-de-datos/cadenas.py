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
#formateo de float "{valor: width.precicision f}"
print("Los resultados son {r:1.5f}".format(r=resultados))

nombre = "Erick"
edad = 36
print(f"Los resultados son {nombre} con edad de {edad}")
