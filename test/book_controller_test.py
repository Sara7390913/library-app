from model.book import Book
from controller.book_controller import BookController

book_controller = BookController()

book1 = Book(1, "python","Sara", 250, "Test publisher", "programming", "persian")

book_controller.save(book1)

books = book_controller.find_all()

print("Number of books:", len(books))

for book in books:
    print(book.title)