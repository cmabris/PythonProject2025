import os

ruta = os.getcwd()
print(ruta)

os.chdir("/Users/carlos/Desktop/pruebas")
archivo = open("otro_archivo.txt")
print(archivo.read())
archivo.close()

# Podemos crear directorios
os.mkdir("nuevo_directorio")
ruta2 = os.getcwd()
print(ruta2)

# Podemos cambiar de directorio
elemento = os.path.basename(ruta + "/prueba1.txt")
ruta3 = os.path.dirname(ruta + "/prueba1.txt")
print(ruta3)
print(elemento)

# Y si queremos los dos a la vez
elemento = os.path.split(ruta + "/prueba1.txt")
print(elemento)

# Borrar directorios
os.rmdir("nuevo_directorio")

# Para trabajar con rutas sin importar el S.O.
from pathlib import Path
print('Cambiando la ruta con Path')
base_dir = os.path.join("Users", "carlos", "Desktop", "pruebas")
archivo_path = os.path.join(base_dir, "otro_archivo.txt")
archivo2 = open(f"/{archivo_path}")
print(archivo2.read())
archivo2.close()
print(archivo_path)