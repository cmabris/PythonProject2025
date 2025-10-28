lista = [5, 10, 15, 20]
print(lista)

for numero in lista:
    print(numero)

print(list(range(5, 101, 5)))

for numero in range(5, 101, 5):
    print(numero)

numero = 1
while numero <= 100:
    if numero % 5 == 0:
        print(numero)
    numero += 1

