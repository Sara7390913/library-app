from model.book import Book
from service.book_service import BookService

book_service = BookService()

book1 = Book(1, "python","Sara", 250, "Test publisher", "programming", "persian")

book_service.save(book1)

books = book_service.find_all()

print("Number of books:", len(books))

for book in books:
    print(book.title)