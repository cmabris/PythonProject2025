mi_lista = [1, 1, 1, 1, 1, 1, 1, 1]
print(len(mi_lista))
print(mi_lista)

class Objeto:
    pass

mi_objeto = Objeto()
print(mi_objeto)
# print(len(mi_objeto))

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"CD: {self.autor} - {self.titulo} ({self.canciones} canciones)"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("CD eliminado")

mi_cd = CD('Queen', 'Greatest Hits', 12)
print(mi_cd)
print(len(mi_cd))
