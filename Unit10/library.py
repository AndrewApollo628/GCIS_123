#Author: Andrew Apollo 

#Import Statements
import csv

#Activity 10.3.5
class Book:
    _slots__ = ["title", "author", "copies"]

    def __init__(self, title:str , author:str, copies:int = 1):
        self.title = title
        self.author = author
        self.copies = copies

#Activity 10.3.6
class Patron:
    __slots__ = ["patron_id", "name", "has", "wants"]

    def __init__(self, patron_id = "000-0000", name = "Reader"):
        self.patron_id= patron_id
        self.name = name 
        self.has = []
        self.wants = list()

#Activity 10.3.7
class CardCatalog:
    __slots__ = ["books_by_title", "books_by_author"]

    def __init__(self):
        self.books_by_title = {} #string title -> book object
        self.books_by_author = {} #string name -> list of book objects 

#Activity 10.3.8
class Library:
    __slots__ = ["on_shelves", "patrons", "card_catalog"]

    def __init__(self, inventory_filename):
        self.on_shelves = []
        self.patrons = [] 
        self.card_catalog = CardCatalog()

        with open(inventory_filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_file)

            for record in csv_reader:
                count = int(record[2])
                book = Book(record[0], record[1], count)
                self.on_shelves.append(book)

                books_by_author = self.card_catalog.books_by_author
                if book.author not in books_by_author:
                    books_by_author[book.author] = [] 
                books_by_author[book.author] += [book]

                books_by_title = self.card_catalog.books_by_title
                if book.author not in books_by_title:
                    books_by_title[book.title] = [] 
                books_by_title[book.title] += [book]

        
LIBRARY = Library("data/books.csv")


def main():

    #Class Activity 10.3.5
    '''
    myBook = Book("Harry Potter","JKRowling", 5 )
    print(myBook.title, myBook.author, myBook.copies)
    '''

    #Class activity 10.3.6
    '''
    aPatron = Patron()
    print(aPatron.patron_id, aPatron.name)
    '''

    #Class activity 10.3.7
    #theCatalog = CardCatalog()

    #Class activity 10.3.8
    patron = Patron("0", "Bruce")
    LIBRARY.patrons.append(patron)
    print(LIBRARY.patrons[0].name)
    print(LIBRARY.on_shelves[10].title, LIBRARY.on_shelves[10].author, LIBRARY.on_shelves[10].copies)

main()