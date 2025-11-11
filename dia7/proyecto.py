class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"{self.nombre} {self.apellido} tiene un balance de {self.balance} en su cuenta {self.numero_cuenta}"

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Deposito aceptado")

    def retirar(self, cantidad):
        if cantidad < self.balance:
            self.balance -= cantidad
            print("Retirada aceptada")
        else:
            print("Operación no permitida, no hay saldo suficiente")

def crear_cliente():
    print("\nVamos a crear un cliente nuevo")
    nombre = input("Nombre del cliente: ")
    apellidos = input("Apellidos del cliente: ")
    numero_cuenta = input("Número de cuenta del cliente: ")
    return Cliente(nombre, apellidos, numero_cuenta)

def menu():
    print("\nMenú")
    print("====")
    print("1. Crear cliente")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Ver cliente")
    print("5. Salir")
    return int(input("Opción: "))

def main():
    cliente = None
    while True:
        opcion = menu()
        if opcion == 1:
            cliente = crear_cliente()
        elif opcion == 2:
            if cliente:
                cantidad = float(input("Cantidad a depositar: "))
                cliente.depositar(cantidad)
            else:
                print("No hay cliente registrado")
        elif opcion == 3:
            if cliente:
                cantidad = float(input("Cantidad a retirar: "))
                cliente.retirar(cantidad)
            else:
                print("No hay cliente registrado")
        elif opcion == 4:
            if cliente:
                print(cliente)
            else:
                print("No hay cliente registrado")
        elif opcion == 5:
            break
        else:
            print("Opción no válida")

main()
