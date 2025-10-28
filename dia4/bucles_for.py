lista = ['a', 'b', 'c']
for letra in lista:
    print(letra)
for letra in lista:
    print('Letra: ' + letra)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

lista = ['pablo', 'laura', 'fede', 'luis', 'julia']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f'No es un nombre que empieza por l: {nombre}')

numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor += numero
print(mi_valor)

palabra = 'python'
for letra in palabra:
    print(letra)

for letra in 'python':
    print(letra)

for letra in ('p', 'y', 't', 'h', 'o', 'n'):
    print(letra)

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for clave in dic:
    print(clave)

for item in dic.items():
    print(item)

for valor in dic.values():
    print(valor)

for clave, valor in dic.items():
    print(f'Clave: {clave} - Valor: {valor}')