from model.book import Book
from model.member import Member
from model.borrow import Borrow

book = Book(1, "Python", "Roya Alipor", 250, "Test publisher", "programming", "persian")

member = Member(1, "Sara", "Ahmadi", 22, "09127195482", "1234567890")

borrow = Borrow(1, member, book, "2026-10-13")

print(borrow.get_info())

print(borrow.is_returned())

borrow.return_book("2026-10-13")

print(borrow.get_info())
print(borrow.is_returned())


#=============================================
# test invalid borrow_id pass
#=============================================

try:
    borrow.borrow_id = -1
except ValueError as e:
    print(e)


#=============================================
# test invalid member pass
#=============================================

try:
    borrow.member = "Sara"
except TypeError as e:
    print(e)


#=============================================
# test invalid book pass
#=============================================

try:
    borrow.book = "python"
except TypeError as e:
    print(e)


#=============================================
# test invalid return date pass
#=============================================

try:
    borrow.return_date = "abc"
except ValueError as e:
    print(e)