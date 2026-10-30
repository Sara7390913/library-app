from tools.logger import Logger
from service.storage_service import StorageService


class StorageController:
    def __init__(self):
        self.storage_service = StorageService()

    def save(self, storage):
        try:
            self.storage_service.save(storage)
            Logger.info("StorageController: storage saved successfully")
        except (ValueError, TypeError) as e:
            Logger.error(f"Error saving storage: {e}")
            raise

    def find_all(self):
        try:
            return self.storage_service.find_all()
        except Exception as e:
            Logger.error(f"Error finding storage: {e}")
            raise
