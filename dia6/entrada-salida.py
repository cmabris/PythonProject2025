mi_archivo = open("prueba.txt")

print(mi_archivo.read())

mi_archivo.close()

print('\n')

archivo = open("prueba.txt")
linea = archivo.readline()
print(linea)
linea = archivo.readline()
print(linea)
linea = archivo.readline()
print(linea)
archivo.close()

archivo = open("prueba.txt")
contador = 1
for linea in archivo:
    print(f"Linea {contador}: {linea.rstrip()}")
    contador += 1
archivo.close()

archivo = open("prueba.txt")
lineas = archivo.readlines()
print(type(lineas))
print(lineas)
archivo.close()