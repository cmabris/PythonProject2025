from pathlib import Path

carpeta = Path("/Users/carlos/Desktop/pruebas/otro_archivo.txt")
print(carpeta.exists())
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)
print(carpeta.parent)

from pathlib import PureWindowsPath

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
print(f"C:{ruta_windows}")