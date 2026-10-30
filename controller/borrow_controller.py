from service.borrow_service import BorrowService
from tools.logger import Logger

class BorrowController():
    def __init__(self):
        self.borrow_service = BorrowService()

    def save(self, borrow):
        try:
            self.borrow_service.save(borrow)
            Logger.info(f"BorrowController: borrow saved successfully")
        except(ValueError, TypeError) as e:
            Logger.error(f"Error saving borrow: {e}")
            raise

    def find_all(self):
        try:
            return self.borrow_service.find_all()
        except Exception as e:
            Logger.error(f"Error finding borrow: {e}")
            raise