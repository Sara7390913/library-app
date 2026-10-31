class StorageDa:
    def __init__(self):
        self.__storage_list = []


    def save(self, storage):
        self.__storage_list.append(storage)



    def find_all(self):
        return self.__storage_list

