# Los decoradores son funciones que reciben una función como parámetro
# y devuelven otra función

def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

# si queremos imprimir un mensaje antes y después de la función
print('Hola')
mayuscula('Hoy es un buen día')
print('Adiós')

# Otra alternativa para lo mismo es incluir el mensaje en la función
# pero obliga a repetir código

def mayuscula2(texto):
    print('Hola')
    print(texto.upper())
    print('Adiós')

def minuscula2(texto):
    print('Hola')
    print(texto.lower())
    print('Adiós')

# Podemos definir una función cuyo argumento sea otra función
def una_funcion(funcion):
    return funcion

# Podemos llamar a la función que recibe otra función como argumento
# y pasarle la función que queremos ejecutar
una_funcion(mayuscula('Hola1'))
una_funcion(minuscula('Hola2'))

# También podemos definir una función que contenga otras funciones
def cambiar_letras(tipo):
    def mayuscula3(texto):
        print(texto.upper())

    def minuscula3(texto):
        print(texto.lower())

    if tipo =='may':
        return mayuscula3
    elif tipo == 'min':
        return minuscula3

operacion = cambiar_letras('min')

operacion('Hola3')

# Decoradores
# Los decoradores son funciones que reciben una función como parámetro
# y devuelven otra función

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adiós')

    return otra_funcion

# Para decorar una función, se pone el decorador encima de la función que
# queremos decorar. Pero supone que siempre aparecerá la función decorada
# con los mismos saludos

@decorar_saludo
def mayuscula4(texto):
    print(texto.upper())

@decorar_saludo
def minuscula4(texto):
    print(texto.lower())

mayuscula4('Python')
minuscula4('Python')