# Las tuplas son similares a las listas, pero son inmutables
# Ocupan menos espacio en memoria y son más rápidas
# Se definen con paréntesis

mi_tupla = (1, 2, 3, 4)
print(type(mi_tupla))

mi_tupla = 1, 2, 3, 4, 5
print(type(mi_tupla))

t = (5, 5.6, 'ff')
print(t)

print(mi_tupla[0])
print(mi_tupla[-2])

# mi_tupla[0] = 10

# mi_tupla.append(6)

mi_tupla = (1, 2, (10, 20), 4)
print(mi_tupla[2])
print(mi_tupla[2][1])

mi_tupla = list(mi_tupla)
print(type(mi_tupla))

t = (1 ,2, 3)
x, y, z = t
print(x, y, z)

t = (1 ,2, 3, 1)
print(len(t))
print(t.count(1))
print(t.index(1))
