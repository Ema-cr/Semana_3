library = []
def Menu():
    print ("""Welcome to the Riwi Library!, what you want to do?:
    -----------------------Menu---------------------------
    1.Add a Book." 
    2.Search a book by title.
    3.Register a book loan.
    4.Return books.
    5.Delete books from the catalog.
    6.Show the books for genre.
    7.Show inventory summary.""")

def Add_book():
    while True:
        while True:
            name_book =str (input("Enter the name of the book: "))
            author_name =str (input("Enter the author's names: "))
            try:
                if author_name.isnumeric():
                    print ("Please enter a valid name of the author. ")
                else:
                    break
            except ValueError:
                print ("Please enter a valid value. ")
        while True: 
            try:
                number_copies=int(input("Number of copies available: "))
                if number_copies < 0:
                        print("Please enter a valid quantity. ")
                else:
                    break
            except ValueError:
                    print("Please enter a valid number. ")
        while True:
            try:
                literary_genre=str(input("Enter the Literary genre of the book: "))
                if literary_genre.isnumeric():
                        print ("Please enter a valid genre of the book. ")
                else:
                    break
            except ValueError:
                    print ("Please enter a valid genre. ")

        books = {
            "name": name_book,
            "author": author_name,
            "copies": number_copies,
            "genre" : literary_genre
        }

        library.append(books)
        break
    print (library)


def find_a_book():
     
Add_book()
