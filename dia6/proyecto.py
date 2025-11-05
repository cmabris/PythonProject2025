from pathlib import *
#from unicodedata import category
from os import system

def get_recipes_path():
    return Path(Path.home().cwd(), 'recetas')

def get_category_path(category):
    return Path(get_recipes_path(), category)

def get_recipe_path(category, recipe):
    return Path(get_category_path(category), recipe + '.txt')

def welcome():
    print("Bienvenido al libro de recetas\n")
    print("La ruta de acceso a la carpeta de recetas es: ")
    recipes_path = get_recipes_path()
    print(recipes_path)
    cantidad = Path(recipes_path).glob('**/*.txt')
    print(f"En la carpeta de recetas hay {len(list(cantidad))} recetas\n")

def menu():
    print("Menú de opciones:")
    print("1. Mostrar receta")
    print("2. Añadir receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir\n")
    opcion = input("Introduce el número de la opción que deseas realizar: ")
    return opcion

def select_category():
    print("Las categorías de recetas disponibles son: ")
    recipes_path = get_recipes_path()
    for category in Path(recipes_path).iterdir():
        print(category.name)
    print("\n")
    category = input("Introduce el nombre de la categoría de la receta que deseas consultar: ")
    return category, get_category_path(category)

def show_recipe():
    category, category_path = select_category()
    print(f"Las recetas de la categoría {category} son: ")
    for recipe in Path(category_path).iterdir():
        print(recipe.stem)
    recipe = input("Introduce el nombre de la receta que deseas consultar: ")
    recipe_path = get_recipe_path(category, recipe)
    print("\n")
    print(recipe_path.read_text())
    print("\n")

def add_recipe():
    category, category_path = select_category()
    recipe = input("Introduce el nombre de la receta que deseas añadir: ")
    recipe_path = get_recipe_path(category, recipe)
    recipe_path.touch()
    content = input("Introduce el contenido de la receta: ")
    recipe_path.write_text(content)
    print("Receta añadida correctamente\n")

def create_category():
    category = input("Introduce el nombre de la categoría que deseas crear: ")
    category_path = get_category_path(category)
    category_path.mkdir()
    print("Categoría creada correctamente\n")

def delete_recipe():
    category, category_path = select_category()
    recipe = input("Introduce el nombre de la receta que deseas eliminar: ")
    recipe_path = get_recipe_path(category, recipe)
    recipe_path.unlink()
    print("Receta eliminada correctamente\n")

def delete_category():
    category, category_path = select_category()
    category_path.rmdir()
    print("Categoría eliminada correctamente\n")

welcome()
opcion = menu()
while opcion != "6":
    if opcion == "1":
        show_recipe()
    elif opcion == "2":
        add_recipe()
    elif opcion == "3":
        create_category()
    elif opcion == "4":
        delete_recipe()
    elif opcion == "5":
        delete_category()
    input()
    system("clear")
    opcion = menu()
print("Gracias por usar el programa")

