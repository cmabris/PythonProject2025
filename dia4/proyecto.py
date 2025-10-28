from random import randint

nombre = input("Introduce tu nombre: ")
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100,\ny tienes solo ocho intentos para adivinar cuál crees que es.")
print("¡Buena suerte!")

numero_secreto = randint(1, 100)
numero = 0

for intentos in range(1,9):
    print(f"Intento {intentos}: ")
    numero = int(input("Introduce un número: "))
    if numero == numero_secreto:
        print(f"¡Felicidades, {nombre}! ¡Has adivinado el número!")
        print(f"Has usado {intentos} intentos.")
        break
    elif numero not in range(1, 101):
        print("El número debe estar entre 1 y 100.")
    elif numero < numero_secreto:
        print("El número introducido es menor que el numero secreto.")
    else:
        print("El número introducido es mayor que el numero secreto.")

if numero != numero_secreto:
    print(f"Lo siento, {nombre}, el número secreto era {numero_secreto}.")

intentos = 0

while intentos < 8:
    intentos += 1
    print(f"Intento {intentos}: ")
    numero = int(input("Introduce un número: "))
    if numero == numero_secreto:
        print(f"¡Felicidades, {nombre}! ¡Has adivinado el número!")
        print(f"Has usado {intentos} intentos.")
        break
    elif numero not in range(1, 101):
        print("El número debe estar entre 1 y 100.")
    elif numero < numero_secreto:
        print("El número introducido es menor que el numero secreto.")
    else:
        print("El número introducido es mayor que el numero secreto.")

if numero != numero_secreto:
    print(f"Lo siento, {nombre}, el número secreto era {numero_secreto}.")

print("¡Gracias por jugar!")