def multiplicar(numero1, numero2):
    return numero1 * numero2

resultado = multiplicar(5, 6)
print(resultado)

resultado = multiplicar(2.5, 3.12)
print(resultado)

resultado = multiplicar('hola', 3)
print(resultado)

#resultado = multiplicar('hola', 'mundo')
#print(resultado)

def invertir_palabra(palabra):
    return palabra[::-1].upper()

print(invertir_palabra('hola'))
print(invertir_palabra('Dabale arroz a la zorra el abad'))