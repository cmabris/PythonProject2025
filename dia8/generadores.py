# Las funciones generadoras son funciones que contienen una palabra yield
# Sirven para generar una secuencia de valores en lugar de devolver un único valor
# Devuelve un objeto generador que es iterable

def mi_funcion():
    return 4

def mi_generador():
    yield 4

print(mi_generador())
g = mi_generador()
print(mi_funcion())
print(next(g))

def mi_funcion2():
    return 4

def mi_generador2():
    num = 4
    while True:
        yield num
        num += 1

g2 = mi_generador2()
print(mi_funcion2())
print(next(g2))
print(mi_funcion2())
print(next(g2))

# Otro ejemplo pero trabajando con listas
def mi_funcion3():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista

def mi_generador3():
    for x in range(1, 5):
        yield x * 10

print(mi_funcion3())
print(mi_generador3())
g3 = mi_generador3()
print(next(g3))
print(next(g3))

# Otro ejemplo
def mi_generador4():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g4 = mi_generador4()
print(next(g4))
print(next(g4))
print(next(g4))
# print(next(g4))
