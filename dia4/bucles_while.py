monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print('No tengo más monedas')

respuesta = 's'
while respuesta == 's':
    respuesta = input('Quieres continuar? (s/n) ')
else:
    print('Gracias por participar')

while respuesta == 's':
    # Escribir el menú
    pass

nombre = input('Introduce tu nombre: ')
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)