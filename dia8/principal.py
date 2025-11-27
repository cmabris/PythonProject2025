import numeros

def preguntar():
    while True:
        print("\nBienvenido/a/e a la Farmacia")
        print("[P] Turno Perfumeria")
        print("[F] Turno Farmacia")
        print("[C] Turno Cosmética")

        try:
            opcion = input("Introduce una opción: ").upper()
            ['P', 'F', 'C'].index(opcion)
        except ValueError:
            print("Introduce una opción válida")
        else:
            break
    numeros.decorar_turno(opcion)

def inicio():
    while True:
        preguntar()
        try:
            respuesta = input("¿Desea otro turno? [S/N]: ").upper()
            ['S', 'N'].index(respuesta)
        except ValueError:
            print("Introduce la opción correcta")
        else:
            if respuesta == 'N':
                print("Gracias por venir a la Farmacia")
                break

inicio()

