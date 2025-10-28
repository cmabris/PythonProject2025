texto = "Este es el texto de Federico"
resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.capitalize()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"

resultado = " ".join([a, b, c, d])
print(resultado)

resultado = "-".join([a, b, c, d])
print(resultado)

resultado = texto.find("s")
print(resultado)

resultado = texto.find("z")
print(resultado)

# resultado = texto.index("z")
# print(resultado)

resultado = texto.find("Federico")
print(resultado)

resultado = texto.find("e", 4, 10)
print(resultado)

resultado = texto.replace("Federico", "Juan")
print(resultado)

resultado = (texto.replace("a", "e")
             .replace("i", "e")
             .replace("o", "e")
             .replace("u", "e"))
print(resultado)
