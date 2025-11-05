class Pajaro:
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

piolin = Pajaro('amarillo', 'canario')
print(piolin.color)
print(piolin.especie)

print(f"El pájaro es un {piolin.especie} de color {piolin.color}")

# También tenemos atributos de clase
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('Negro', 'Periquito')
print(f"El pájaro es un {piolin.especie} de color {piolin.color}")
print(Pajaro.alas)
print(mi_pajaro.alas)