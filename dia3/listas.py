mi_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(mi_lista)

otra_lista = ['hola', 55, 6.1]
print(otra_lista)
print(type(otra_lista))

resultado = mi_lista[0]
print(resultado)

resultado = mi_lista[2:5]
print(resultado)

resultado = mi_lista[::-1]
print(resultado)

mi_lista2 = ['h', 'i', 'j', 'k', 'l']
print(mi_lista + mi_lista2)

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

otra_lista[0] = 'hola mundo'
print(otra_lista)

otra_lista.append('new item')
print(otra_lista)

otra_lista.pop(1)
print(otra_lista)

mi_lista4 = mi_lista2 + mi_lista
print(mi_lista4)
mi_lista4.sort()
print(mi_lista4)
mi_lista4.reverse()
print(mi_lista4)

mi_lista5 = mi_lista2 + mi_lista
mi_lista5.sort(reverse=True)
print(mi_lista5)

# No se puede ordenar elementos no comparables
# otra_lista.sort()
# print(otra_lista)
