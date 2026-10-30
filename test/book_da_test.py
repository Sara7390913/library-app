from model.book import Book
from data_access.book_da import BookDA

book_da = BookDA()

book1 = Book(1, "python","Sara", 250, "Test publisher", "programming", "persian")
book2 = Book(2, "OOP", "Ali", 300, "Test publisher", "Education", "English")

book_da.save(book1)
book_da.save(book2)

books = book_da.find_all()

print("Number of books:", len(books))

for book in books:
    print(book.title)