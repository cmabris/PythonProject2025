diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)
resultado = diccionario['c2']
print(resultado)

cliente = {'nombre': 'Juan', 'apellido': 'Fuentes', 'peso': 88, 'talla':1.76}
consulta = cliente['apellido']
print(consulta)

# consulta = cliente['edad']
# print(consulta)

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'a': 1, 'b': 2}}
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3'])
print(dic['c3']['a'])

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper())
print(dic['c1'][0].upper())

dic = {1: 'a', 2: 'b'}
print(dic)
dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())