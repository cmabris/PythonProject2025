if 10 > 9:
    print("10 es mayor que 9")

x = True
if x:
    print("x es verdadero")

if 5 == 2:
    print("5 es igual a 2")
else:
    print("5 no es igual a 2")

mascota = 'perro'
if mascota == 'gato':
    print("Es un gato")
else:
    print("No sé que animal tienes")

mascota = 'perro'
if mascota == 'gato':
    print("Es un gato")
elif mascota == 'perro':
    print("Es un perro")
else:
    print("No sé que animal tienes")

edad = 16
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

edad = 16
calificacion = 9
if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 5:
        print('Aprobado')
    else:
        print('Suspenso')
else:
    print("Eres mayor de edad")
    if calificacion >= 5:
        print('Aprobado')
    else:
        print('Suspenso')