nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]

combinados = zip(nombres, edades)
print(combinados)
print(type(combinados))
print(list(combinados))

nombres = ['Ana', 'Hugo', 'Valeria', 'Juan']
edades = [65, 29, 42]
print(list(zip(nombres, edades)))

ciudades = ['Madrid', 'Barcelona', 'Bilbao']
print(list(zip(nombres, edades, ciudades)))

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

for nombre, edad, ciudad in list(zip(nombres, edades, ciudades)):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
