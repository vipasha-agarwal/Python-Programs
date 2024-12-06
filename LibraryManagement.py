class Library:
    def __init__(self):
        self.noBooks = 0
        self.Books = []
    def addBooks(self, book):
        self.Books.append(book)
        self.noBooks = len(self.Books)
    def showInfo(self):
        print(f"The Library has {self.noBooks} books. This books are {self.Books}")

l1 = Library()
l1.addBooks("Harry Potter")
l1.addBooks("Harry Potter1")
l1.addBooks("Harry Potter2")
l1.addBooks("Harry Potter3")
l1.addBooks("Harry Potter4")
l1.addBooks("Harry Potter5")
l1.showInfo()

