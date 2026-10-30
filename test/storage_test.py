from model.storage import Storage
from model.book import Book

storage = Storage(1, "room A", 3, book=[])

book1 = Book(1, "Python", "Roya Alipor", 250, "Test publisher", "programming", "English")
book2 = Book(2, "OOP", "Sara Hashemi", 200, "Test publisher", "programming", "English")
book3 = Book(3, "Django", "Roya Alipor", 300, "Test publisher", "programming", "Persian")

storage.add_book(book1)
storage.add_book(book2)
storage.add_book(book3)

print("Number of books:", len(storage.get_book()))

book4 = Book(4, "Java", "Ali Alipor", 180, "Test publisher", "programming", "English")

#=============================================
# test add_book and capacity pass
#=============================================

try:
    storage.add_book(book4)
except ValueError as e:
    print(e)
#=============================================
# test remove_book pass
#=============================================

storage.remove_book(book1)
print("Book after removing book1:")
for book in storage.get_book():
    print(book.title)

#=============================================
# test find_book pass
#=============================================
found_book = storage.find_book(2)

if found_book:
    print("Found book:", found_book.title)
else:
    print("Book not found")

#=============================================
# test capacity pass
#=============================================
try:
    storage.capacity = -5
except ValueError as e:
    print(e)

#=============================================
# test book pass
#=============================================
print("\n--- Test invalid book list ---")

try:
    storage.book = "not a list"
except ValueError as e:
    print(e)