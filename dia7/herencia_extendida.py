class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('He nacido')

    def hablar(self):
        print('Este animal hace ruido')

class Pajaro(Animal):
    # Añadimos atributos a la clase hija. 1ª forma
    # def __init__(self, edad, color, altura_vuelo):
    #    self.edad = edad
    #    self.color = color
    #    self.altura_vuelo = altura_vuelo

    # Añadimos atributos a la clase hija. 2ª forma
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pío pío")

    def volar(self, metros):
        print(f"Este pájaro vuela {metros} metros")

piolin = Pajaro(3, 'amarillo', 60)
piolin.nacer()
piolin.hablar()
piolin.volar(50)

print(piolin.altura_vuelo)
animal = Animal(5, 'naranja')
animal.hablar()
# animal.volar(50)



