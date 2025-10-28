from random import shuffle

palitos = ['-', '--', '---', '----']

def mezclar_palitos(lista):
    shuffle(lista)
    return lista

def pedir_palito():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')
    return int(intento)

def comprobar_palito(lista, eleccion):
    if lista[eleccion - 1] == '-':
        print("¡Has perdido!")
    else:
        print("¡Has ganado!")
    print(f"Te ha tocado el palito {lista[eleccion - 1]}")

#palitos_mezclados = mezclar_palitos(palitos)
#eleccion = pedir_palito()
comprobar_palito(
    mezclar_palitos(palitos),
    pedir_palito()
)