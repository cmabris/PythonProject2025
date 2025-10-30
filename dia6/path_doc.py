from pathlib import Path

# La ruta que genera Path es relativa
guia = Path("Barcelona", "Sagrada_Familia", "entrada.txt")
print(guia)

base = Path.home()
print(base)
guia2 = Path(base, "Barcelona", "Sagrada_Familia", "entrada.txt")
print(guia2)

# El constructor de Path maneja diferentes entradas de parámetros
guia3 = Path(base, "Europa", "Espana", Path("Barcelona", "Sagrada_Familia", "entrada.txt"))
print(guia3)

# Podemos cambiar el nombre el archivo manteniendo la ruta
guia4 = guia3.with_name("salida.txt")
print(guia4)

# Podemos obtener la carpeta contenedora
print(guia4.parent)
print(guia4.parent.parent)

print("Trabajando con la carpeta Europa")
base = Path.home()
guia5 = Path(base, "Desktop", "Europa")
print(guia5)
for file in Path(guia5).glob("*.txt"):
    print(file)

print("\n")

# Y para obtener todos los archivos
for file in Path(guia5).glob("**/*.txt"):
    print (file)

print("\n")

# Para obtener los archivos desde un lugar concreto
guia6 = Path(base, "Desktop", "Europa", "Espana", "Barcelona", "Sagrada_Familia")
en_europa = guia6.relative_to(Path(base, "Desktop", "Europa"))
en_espana = guia6.relative_to(Path(base, "Desktop", "Europa", "Espana"))
print(en_europa)
print(en_espana)




