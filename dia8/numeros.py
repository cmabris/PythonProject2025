"""
Módulo que contiene los generadores y el decorador del proyecto
"""

def turno_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n:02}"

def turno_farmacia():
    for n in range(1, 10000):
        yield f"F - {n:02}"

def turno_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n:02}"

p = turno_perfumeria()
f = turno_farmacia()
c = turno_cosmetica()

def decorar_turno(seccion):
    print("\n" + "-" * 30)
    print("Su número es: ")
    if seccion == 'P':
        print(next(p))
    elif seccion == 'F':
        print(next(f))
    else:
        print(next(c))
    print("Espere y será atendido/a/e")
    print("-" * 30)
    