from model.book import Book
from model.member import Member
from model.borrow import Borrow
from data_access.borrow_da import BorrowDA


borrow_da = BorrowDA()

book = Book(1, "python","Sara", 250, "Test publisher", "programming", "persian")
member = Member(1, "Sara", "Ahmadi", 22, "09127195482", "1234567890")

borrow = Borrow(1, member, book, "2026-10-20")

borrow_da.save(borrow)

borrows = borrow_da.find_all()

print("Number of borrows: ", len(borrows))

for item in borrows:
    print(item.book.title, item.member.name )
    