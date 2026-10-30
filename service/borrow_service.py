from data_access.borrow_da import BorrowDA
from tools.logger import Logger

class BorrowService:
    def __init__(self):
        self.borrow_da = BorrowDA()

    def save(self, borrow):
        self.borrow_da.save(borrow)
        Logger.info(f"BorrowService: borrow saved - "
                    f"{borrow.book.title} by {borrow.member.name}")


    def find_all(self):
        return self.borrow_da.find_all()