# Define una clase llamada “Libro” con los siguientes atributos: titulo, autor, genero y
# puntuacion (valor numérico que representa la popularidad del libro). Crea un método
# __init__ para inicializar estos atributos.

class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion
        
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)        

#Crea una lista llamada lista_libros donde almacenarás los objetos de la clase Libro.
lista_libros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]

def agregar_libro():
    titulo = input('Ingrese el título: ')
    autor = input('Ingrese el autor: ')
    genero = input('Ingrese el género: ')
    puntuacion = input('Ingrese la puntuación: ')
    while True:
        puntuacion = input('Ingrese la puntuación (0.0 - 5.0): ')
        try:
            puntuacion = float(puntuacion)
            if 0 <= puntuacion <= 5:
                break
            else:
                print("La puntuación debe estar entre 0 y 5.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")
    libro_nuevo = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(libro_nuevo)
    print("El libro ha sido agregado correctamente.")

def filtrar_por_genero():
    generos_disponibles = []
    for n in lista_libros:
        if n.genero not in generos_disponibles:
            generos_disponibles.append(n.genero)
        else:
            continue
    print(f'Los géneros disponibles son: {generos_disponibles}')
    genero_buscado = input("Selecciones un género:")
    libros_filtrados = [libro for libro in lista_libros if libro.genero.lower() == genero_buscado.lower()]
    if libros_filtrados:
        print(f"\nLibros del género '{genero_buscado}':")
        for libro in libros_filtrados:
            print(f"- {libro.titulo} de {libro.autor} (Puntuación: {libro.puntuacion})")
    else:
        print(f"No hay libros del género '{genero_buscado}'.")
    print("\n")

def recomendar():
    generos_disponibles = []
    for n in lista_libros:
        if n.genero not in generos_disponibles:
            generos_disponibles.append(n.genero)
        else:
            continue
    print(f'\nLos géneros disponibles son: {generos_disponibles}')
    genero_buscado = input("Selecciones un género:")
    libro_ideal = [libro for libro in lista_libros if libro.genero.lower() == genero_buscado.lower()]
    libro_ideal.sort(key = lambda libro: libro.puntuacion, reverse=True)
    print(f'\nRecomendación para el género {genero_buscado.lower()}\n-Título: {libro_ideal[0].titulo} \n-Puntuación (sobre 5): {libro_ideal[0].puntuacion}')
    print("\n")

def opciones():
    while True:
        options = {
                1:'Agregar libro',
                2:'Buscar un libro por género',
                3:'Recomendar libro',
                4:'Salir'
                }
        print(f'''¿Qué desea hacer?\n\n1. {options[1]}\n2. {options[2]}\n3. {options[3]}\n4. {options[4]}\n''')
        opcion_elegida = input('Elija una opción (por número) de la lista de arriba (ej: Agregar libro ---> 1): ')
        while not (opcion_elegida.isnumeric() in options.keys()):
            opcion_elegida = input('Elija una opción (por número) de la lista de arriba (ej: Agregar libro ---> 1): ')    
        if int(opcion_elegida) == 1:
            agregar_libro()
        elif int(opcion_elegida) == 2:
            filtrar_por_genero()
        elif int(opcion_elegida) == 3:
            recomendar()
        else:
            print("¡Adiós!")
            break
        
opciones()