class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pío pío, mi color es {}' . format(self.color))

    # Los métodos de instancia pueden acceder a otros métodos
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")
        self.piar()

    # Los métodos de instancia pueden acceder y modifica a los atributos de instancia
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora mi color es {self.color}")

    # También existen los llamados métodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(cls.alas)

    # También existen los métodos estáticos
    # No pueden acceder a los atributos de clase e instancia
    # No pueden acceder a los métodos de clase e instancia
    @staticmethod
    def mirar():
        print("El pájaro mira")

piolin = Pajaro('amarillo', 'canario')
piolin.pintar_negro()
piolin.volar(50)

# Se pueden modificar atributos de clase
# Si se modifica desde un objeto, solo le afecta a él
# piolin.alas = False
# Si se modifica desde la clase, afecta a todos los objetos
Pajaro.alas = False
print(piolin.alas)
print(Pajaro.alas)

# Los métodos de clase no necesitan de instancia
Pajaro.poner_huevos(5)

# Los métodos estáticos pueden ser llamados sin instancia
Pajaro.mirar()


