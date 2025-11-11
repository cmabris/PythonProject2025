def suma():
    n1 = int(input("Introduzca el primer numero: "))
    n2 = int(input("Introduzca el segundo numero: "))
    print(n1 + n2)
    #print("Gracias por sumar")

def suma2():
    try:
        n1 = int(input("Introduzca el primer numero: "))
        n2 = int(input("Introduzca el segundo numero: "))
        print(n1 + n2)
    except ValueError:
        print("Introduce un numero valido")
    else:
        print("Gracias por sumar")
    finally:
        print("Finalizada la suma de dos números")

# 2ª Forma: Podemos hacer un try except en el main para que el programa no se detenga

try:
    suma()
except:
    print("Ha ocurrido un error")
else:
    print("Gracias por sumar")
finally:
    print("Esto fue todo, FIN")

# Podemos manejar errores específicos
# Error1: Concatenamos un string con un número
# Error2: Introducimos un caracter en lugar de un número

def suma3():
    n1 = int(input("Introduzca el primer numero: "))
    n2 = int(input("Introduzca el segundo numero: "))
    print(n1 + n2)
    print("Gracias por sumar " + n1)

try:
    suma3()
except TypeError:
    print("Estás intentando concatenar un string con un número")
except ValueError:
    print("Introduce un numero valido")
else:
    print("Gracias por sumar")
finally:
    print("Esto fue todo, FIN")

def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número: "))
        except ValueError:
            print("Introduce un número válido")
        else:
            print(f"Has introducido el número {numero}")
            break
    print("Gracias por introducir un número")

pedir_numero()
