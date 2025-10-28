texto = input("Introduce un texto: ")
letra1 = input("Introduce una letra: ")
letra2 = input("Introduce otra letra: ")
letra3 = input("Introduce otra letra más: ")

texto_pequeno = texto.lower()
letra1_pequena = letra1.lower()
letra2_pequena = letra2.lower()
letra3_pequena = letra3.lower()

lista_letras = [letra1_pequena, letra2_pequena, letra3_pequena]

lista_texto = list(texto_pequeno)
contador1 = lista_texto.count(letra1_pequena)
contador2 = lista_texto.count(letra2_pequena)
contador3 = lista_texto.count(letra3_pequena)

print(f"La letra {letra1} aparece {contador1} veces en el texto")
print(f"La letra {letra2} aparece {contador2} veces en el texto")
print(f"La letra {letra3} aparece {contador3} veces en el texto")

palabras = texto.split()
print("El número de palabras en el texto es: ", len(palabras))

print('La primera letra del texto es: ', texto[0])
print('La última letra del texto es: ', texto[-1])

palabras_al_reves = palabras[::-1]
texto_al_reves = " ".join(palabras_al_reves)
print("El texto al revés es: ", texto_al_reves)

is_python = "python" in texto_pequeno
diccionario = {True: "Si", False: "No"}
print('¿Está la palabra "python" en el texto? ', diccionario[is_python])