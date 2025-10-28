num1 = 20
num2 = 30.5
print(type(num1))
print(type(num2))

#Conversión implícita
num1 = num1 + num2
print(type(num1))
print(type(num2))

# Conversiones explícitas
num1 = 5.8
print(type(num1))

num2 = int(num1)
print(type(num2))

edad = input("Dime tu edad: ")
print("Tu edad es " + edad)
print(type(edad))
edad = int(edad)
edad = edad + 1
print(edad)


