from model.book import Book
from model.member import Member
from model.borrow import Borrow
from service.borrow_service import BorrowService

borrow_service = BorrowService()

book = Book(1, "python","Sara", 250, "Test publisher", "programming", "persian")

member = Member(1, "Sara", "Ahmadi", 22, "09127195482", "1234567890")

borrow = Borrow(1, member, book, "2026-10-20")

borrow_service.save(borrow)

borrows = borrow_service.find_all()

print("Number of borrows: ", len(borrows))

for item in borrows:
    print(item.book.title, item.member.name)