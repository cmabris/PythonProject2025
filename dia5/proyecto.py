import random

lista_palabras = ['portatil', 'teclado', 'raton', 'monitor', 'impresora', 'altavoces']
letras_acertadas = []
letras_falladas = []

def elegir_palabra(lista):
    return random.choice(lista)

def pedir_letra():
    return input('Introduce una letra: ')

def verificar_letra(palabra, letra):
    if letra in palabra:
        return True
    else:
        return False

def mostrar_palabra(palabra, letras_acertadas):
    palabra_mostrada = ''
    for letra in palabra:
        if letra in letras_acertadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += '_'
    return palabra_mostrada

def vidas_restantes(letras_falladas):
    return 6 - len(letras_falladas)

palabra = elegir_palabra(lista_palabras)

while vidas_restantes(letras_falladas) > 0 and mostrar_palabra(palabra, letras_acertadas) != palabra:
    letra = pedir_letra()
    if verificar_letra(palabra, letra):
        letras_acertadas.append(letra)
    else:
        letras_falladas.append(letra)
    print(mostrar_palabra(palabra, letras_acertadas))
    print(f'Vidas restantes: {vidas_restantes(letras_falladas)}')

if mostrar_palabra(palabra, letras_acertadas) == palabra:
    print('Has ganado!!!')
elif vidas_restantes(letras_falladas) == 0:
    print('Has perdido!!!')
