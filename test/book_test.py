from model.book import Book

book = Book(1, "python", "Roya Alipor", 250, "Danesh", "programming", "English")
book.author = "Sara Hashemi"
book.author = "Sara Hashemi"

print(book.book_id)
print(book.title)
print(book.author)
print(book.page_count)
print(book.publisher)
print(book.category)
print(book.language)

book.author = "Sara Hashemi"

print(book.author)

#=============================================
# test title pass
#=============================================

try:
    book.title = 123
except ValueError as e:
    print(e)

# =============================================
# test page_count pass
# =============================================

try:
    book.page_count = -10
except ValueError as e:
    print(e)

#=============================================
# test author pass
#=============================================

try:
    book.author = 458
except ValueError as e:
    print(e)

#=============================================
# test publisher pass
#=============================================

try:
    book.publisher = 789
except ValueError as e:
    print(e)

#=============================================
# test category pass
#=============================================

try:
    book.category = 654
except ValueError as e:
    print(e)

#=============================================
# test language pass
#=============================================

try:
    book.language = 211
except ValueError as e:
    print(e)

