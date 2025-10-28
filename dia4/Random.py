from random import randint

aleatorio = randint(1, 50)
print(aleatorio)

from random import *

aleatorio = round(uniform(1, 5))
print(aleatorio)

aleatorio = round(uniform(1, 5), 2)
print(aleatorio)

aleatorio = uniform(1, 5)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['rojo', 'verde', 'azul', 'amarillo']
color = choice(colores)
print(color)

numeros = list(range(5, 50, 5))
print(numeros)
shuffle(numeros)
print(numeros)
