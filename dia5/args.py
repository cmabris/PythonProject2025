def suma(a, b):
    return a + b

print(suma(5, 6))

def suma2(*args):
    return sum(args)

print(suma2(5, 6))
print(suma2(5, 6, 7))
print(suma2(5))

def suma3(*numeros):
    return sum(numeros)

print(suma3(5, 6, 7))
