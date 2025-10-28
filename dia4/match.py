serie = 'N-02'

if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Motorola')
else:
    print('No existe ese producto')

# A partir de Python 3.10
match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe ese producto')

cliente = {'nombre': 'Federico', 'edad': 45, 'ocupación': 'Instructor'}
cliente2 = {'nombre': 'Pepe', 'edad': 15, 'ocupación': 'Nini'}
pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'director': 'Lana Wachhowski',
                              'protagonista': 'Keanu Reeves'}}
elementos = [cliente, pelicula, 'libro', cliente2]

for elemento in elementos:
    match elemento:
        case {'nombre': nombre, 'edad': edad, 'ocupación': ocupacion}:
            print(f"Cliente: {nombre}, {edad} años, {ocupacion}")
        case {'titulo': titulo, 'ficha_tecnica': {'director': director, 'protagonista': protagonista}}:
            print(f"Pelicula: {titulo}, dirigida por {director}, protagonizada por {protagonista}")
        case _:
            print(elemento)

