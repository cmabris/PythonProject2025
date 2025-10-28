mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)

resultado = mi_texto[9]
print(resultado)

resultado = mi_texto[-4]
print(resultado)

resultado =mi_texto.index('n')
print(resultado)

# Error si no lo encuentra
# resultado = mi_texto.index('x')
# print(resultado)

resultado = mi_texto.index('prueba')
print(resultado)

resultado = mi_texto.index('a', 5)
print(resultado)

resultado = mi_texto.index('a', 5, 11)
print(resultado)

# Error si no encuentra
# resultado = mi_texto.index('a', 5, 10)
# print(resultado)

resultado = mi_texto.rindex('a')
print(resultado)