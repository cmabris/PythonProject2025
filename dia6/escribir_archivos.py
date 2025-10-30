archivo = open("prueba.txt", "r")
print(archivo.read())
archivo.close()

archivo = open("prueba1.txt", "w")
archivo.write("Hola mundo\n")
archivo.write("Adios mundo cruel\n")
archivo.write("Estoy escribiendo desde Python\n")
archivo.close()

archivo = open("prueba1.txt", "w")
archivo.writelines(["Hola mundoooooo\n", "Adios Mundoooo\n", "Estoy escribiendo desde Python sin querer\n"])
archivo.close()

archivo = open("prueba1.txt", "a")
archivo.write("Esta es una línea añadida\n")
archivo.close()
