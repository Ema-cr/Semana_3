library = []  # Lista para almacenar todos los libros
valid_genres = ["Fiction", "NonFiction", "Science", "Biography", "Children"]  # Lista de géneros válidos

# Función para agregar un nuevo libro a la biblioteca
def add_book():
    # Validar el nombre del libro
    while True:
        name_book = input("Enter the name of the book: ").strip()
        if name_book == "":
            print("The book name cannot be empty. Please try again.")
            continue
        else:
            break

    # Validar el nombre del autor (no puede estar vacío ni contener números)
    while True:
        author_name = input("Enter the author of the book: ").strip()
        if author_name == "":
            print("The author name can't be empty. Please input a valid name.")
            continue
        elif any(char.isdigit() for char in author_name):
            print("You must enter only letters.")
            continue
        else:
            break

    # Validar que el número de copias sea un entero positivo
    while True:
        try:
            number_copies = int(input("Number of copies available: "))
            if number_copies > 0:
                break
            else:
                print("Please enter a valid quantity.")
        except ValueError:
            print("Please enter a valid number.")

    # Mostrar los géneros disponibles
    print("Available genres:", ", ".join(valid_genres))
    
    # Validar que el género ingresado esté en la lista válida
    while True:
        literary_genre = input("Enter the literary genre of the book: ").strip()
        if literary_genre == "":
            print("The genre of the book can't be empty.")
            continue
        elif literary_genre.lower() not in [g.lower() for g in valid_genres]:
            print("Invalid genre. Please choose from the available list.")
            continue
        else:
            # Normalizar el género para mantener capitalización original
            literary_genre = next(g for g in valid_genres if g.lower() == literary_genre.lower())
            break

    # Crear un diccionario con los datos del libro
    book = {
        "name": name_book,
        "author": author_name,
        "copies": number_copies,
        "genre": literary_genre
    }

    # Añadir el libro a la biblioteca
    library.append(book)

    print("Book added successfully.")

# Función para buscar un libro por título
def find_book(book_to_find, library):
    for prod in library:
        if prod["name"].lower() == book_to_find.lower():
            return prod
    return None  # Retorna None si no se encuentra

# Función para prestar un libro (disminuye una copia)
def loan_books(library):
    name_book = input("Enter the name of the book to loan: ").strip()
    book = find_book(name_book, library)
    if book:
        if book["copies"] > 0:
            book["copies"] -= 1  # Disminuir en 1 las copias
            print(f"Loan successfully registered. {book['copies']} copies remain.")
        else:
            print(f"No copies available of '{name_book}' to lend.")
    else:
        print("Book not found in the library.")

# Función para devolver un libro (aumenta una copia)
def return_books(library):
    name_book = input("Enter the name of the book to return: ").strip()
    book = find_book(name_book, library)
    if book:
        book["copies"] += 1  # Aumentar en 1 las copias
        print(f"Book returned successfully. Now there are {book['copies']} copies.")
    else:
        print("This book is not in our library records.")

# Función para eliminar un libro del catálogo
def delete_book(library):
    name_book = input("Enter the name of the book to delete: ").strip()
    book = find_book(name_book, library)
    if book:
        library.remove(book)  # Elimina el libro de la lista
        print("Book deleted from the catalog.")
    else:
        print("Book not found.")

# Función para mostrar libros por género
def show_books_by_genre(library):
    genre = input("Enter the genre to search for: ").strip()
    found = False  #para saber si se encontraron libros
    for book in library:
        if book["genre"].lower() == genre.lower():
            print(f"- {book['name']} by {book['author']} ({book['copies']} copies)")
            found = True
    if not found:
        print("No books found for that genre.")

# Función para mostrar todos los libros y su cantidad
def inventory_summary(library):
    print("\n--- Inventory Summary ---")
    for book in library:
        print(f"{book['name']} by {book['author']} - {book['copies']} copies")

# Función del menú principal
def Menu():
    while True:
        # Mostrar opciones disponibles
        print("""
Welcome to the Riwi Library! What do you want to do?:
------------------------- Menu -------------------------
1. Add a Book
2. Search a book by title
3. Register a book loan
4. Return books
5. Delete books from the catalog
6. Show the books by genre
7. Show inventory summary
8. Quit
""")
        # Solicitar la opción al usuario
        option = input("Choose an option: ").strip()

        # Ejecutar la opción correspondiente
        if option == "1":
            add_book()
        elif option == "2":
            book_to_find = input("What book do you want to find?: ").strip()
            result = find_book(book_to_find, library)
            if result:
                print(f"Found: '{result['name']}' by {result['author']} with {result['copies']} copies.")
            else:
                print("Book not found.")
        elif option == "3":
            loan_books(library)
        elif option == "4":
            return_books(library)
        elif option == "5":
            delete_book(library)
        elif option == "6":
            show_books_by_genre(library)
        elif option == "7":
            inventory_summary(library)
        elif option == "8":
            print("Thank you for using the Riwi Library System!")  # Salida del programa
            break
        else:
            print("Invalid option. Please choose a number between 1 and 8.")

# Ejecutar el menú principal
Menu()
