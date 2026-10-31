class BorrowDA:
    def __init__(self):
        self.__borrow_list = []

    def save(self, borrow):
        found = False

        for index, item in enumerate(self.__borrow_list):
            if item.borrow_id == borrow.borrow_id:
                self.__borrow_list[index] = borrow
                found = True
                break

        if not found:
            self.__borrow_list.append(borrow)

    def find_all(self):
        return self.__borrow_list

    def find_by_id(self, borrow_id):
        for borrow in self.__borrow_list:
            if borrow.borrow_id == borrow_id:
                return borrow


        return None