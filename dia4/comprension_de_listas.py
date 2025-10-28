palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

lista2 = [letra for letra in palabra]
print(lista2)

lista3 = [numero for numero in range(0, 10)]
print(lista3)

lista4 = [numero for numero in range(0,21) if numero % 2 == 0]
print(lista4)

lista5 = [numero/2 for numero in range(0,11)]
print(lista5)

lista6 = [n if n*2>10 else 'no' for n in range(0,21,2)]
print(lista6)

pies = [10, 20, 30, 40, 50]
metros = [round(pie/3.281,1) for pie in pies]
print(metros)



