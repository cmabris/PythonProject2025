mi_bool = 5 == 5
print(mi_bool)

mi_bool = 5 + 5 == 18 - 8
print(mi_bool)

mi_bool = 'blanco' == 'blanco'
print(mi_bool)

mi_bool = 'blanco' == 'Blanco'
print(mi_bool)

mi_bool = 'blanco' == 'Blanco'.lower()
print(mi_bool)

mi_bool = '100' == 100
print(mi_bool)

mi_bool = 100.0 == 100
print(mi_bool)

mi_bool = 100.0 != 100
print(mi_bool)

mi_bool = 5 < 10
print(mi_bool)

mi_bool = 5 > 10
print(mi_bool)

# Comparaciones múltiples
mi_bool = 5 < 10 < 15
print(mi_bool)

mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool = (4 < 5) and (5 == 2 + 3)
print(mi_bool)

texto = 'esta frase es breve'
mi_bool = 'frase' in texto
print(mi_bool)

mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool)

mi_bool = ('frase' in texto) and ('python' in texto)
print(mi_bool)

mi_bool = ('frase' in texto) or ('python' in texto)
print(mi_bool)

mi_bool = not 5 == 5
print(mi_bool)