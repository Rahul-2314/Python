# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.count_books=0
        self.books=[]

    def addBook(self,book):
            self.books.append(book)
            self.noBooks=len(self.books)

    def showInfo(self):
            print(f"This Library Contains {self.noBooks} books.\nThey Are :\n")
            for book in self.books:
                print(book)

b1=Library()
b1.addBook("Rahul")
b1.addBook("Rahul")
b1.addBook("Rahul")
b1.addBook("Rahul")
b1.addBook("Rahul")
b1.showInfo()
