from model.member import Member
from model.book import Book
from model.borrow import Borrow
from controller.borrow_controller import BorrowController

borrow_controller = BorrowController()

member = Member(1, "Sara", "Ahmadi", 22, "09127195482", "1234567890")

book= Book(1, "python","Sara", 250, "Test publisher", "programming", "persian")

borrow = Borrow(1, member, book, "2026-10-20")

borrow_controller.save(borrow)

borrows = borrow_controller.find_all()

print("Number of borrows: ", len(borrows))

for item in borrows:
    print(item.book.title, item.member.name)