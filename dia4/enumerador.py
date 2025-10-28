lista = ['a', 'b', 'c']
indice = 0
for letra in lista:
    print(f"Letra {indice}: {letra}")
    indice += 1

for indice, letra in enumerate(lista):
    print(f"Letra {indice}: {letra}")

for indice, letra in enumerate(lista, 1):
    print(f"Letra {indice}: {letra}")

for indice, item in enumerate(range(10, 20, 2)):
    print(f"{indice}: {item}")

for indice, item in enumerate(range(10, 20, 2), 1):
    print(f"{indice}: {item}")

# Transformando lista en tuplas
lista = ['a', 'b', 'c', 'd', 'e']
mis_tuplas = list(enumerate(lista))
print(mis_tuplas)

print(mis_tuplas[1][1])