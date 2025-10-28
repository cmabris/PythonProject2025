def chequear_3_cifras(numero):
    return numero in range(100, 1000)

resultado = chequear_3_cifras(658)
print(resultado)

resultado = chequear_3_cifras(65)
print(resultado)

resultado = chequear_3_cifras('Numero')
print(resultado)

def chequear_3_cifras_v2(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass

resultado = chequear_3_cifras_v2([58, 99, 990, 5860])
print(resultado)
print(type(resultado))

resultado = chequear_3_cifras_v2([58, 99, 5860])
print(resultado)

# Ahora queremos que devuelva una lista formada por
# todos los números de tres cifras

def chequear_3_cifras_v3(lista):
    tres_cifras = []
    for n in lista:
        if n in range(100, 1000):
            tres_cifras.append(n)
    return tres_cifras

resultado = chequear_3_cifras_v3([58, 99, 990, 5860, 666, 44, 333])
print(resultado)

resultado = chequear_3_cifras_v3([58, 99, 5860, 44])
print(resultado)
