from data_access.storage_da import StorageDa
from tools.logger import Logger


class StorageService:
    def __init__(self):
        self.storage_da = StorageDa()

    def save(self, storage):
        self.storage_da.save(storage)
        Logger.info(f"StorageService: storage saved - {storage.location} ")

    def find_all(self):
        return self.storage_da.find_all()