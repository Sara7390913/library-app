from model.storage import Storage
from tools.logger import Logger
import json
import os

class StorageDa:
    def __init__(self):
        self.__storage_list = []
        self.__file_name = "storages.json"

        if os.path.isfile(self.__file_name):
            try:
                with open(self.__file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)

                for item in data:
                    storage = Storage(item["storage_id"],
                                      item["location"],
                                      item["capacity"],
                                      [])

                    self.__storage_list.append(storage)

            except (json.JSONDecodeError, OSError, KeyError, TypeError) as error:
                Logger.error(f"Error loading storage: {error}")

    def save(self, storage):
        self.__storage_list.append(storage)

        data = []

        for storage in self.__storage_list:
            data.append({
                "storage_id": storage.storage_id,
                "location": storage.location,
                "capacity": storage.capacity,
            })
        try:
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            Logger.info(f"Storage saved: {storage.location}")
        except OSError as error:
            Logger.error(f"Error saving storage: {error}")
            raise

    def find_all(self):
        return self.__storage_list

