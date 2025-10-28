def suma(**kwargs):
    print(type(kwargs))

suma(x=3, y=5, z=2)

def suma2(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

suma2(x=3, y=5, z=2)

def suma3(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma3(x=3, y=5, z=2))

def suma4(**kwargs):
    return sum(kwargs.values())

print(suma4(x=3, y=5, z=2))

def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    for arg in args:
        print(f"arg: {arg}")
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(1, 2, 3, 4, 5, x=6, y=7)
prueba(1, 2, x=6, y=7)

tupla = (10, 20, 30)
dic = {'clave1':1, 'clave2':2}
prueba(1, 2, tupla, dic)
prueba(1, 2, *tupla, **dic)

args = (10, 20, 30)
kwargs = {'clave1':1, 'clave2':2}
prueba(1, 2, *args, **kwargs)

