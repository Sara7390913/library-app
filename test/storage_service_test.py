from model.storage import Storage
from service.storage_service import StorageService

storage_service = StorageService()

storage1 = Storage(1, "Tehran", 10, [])
storage2 = Storage(2, "Tabriz", 20, [])

storage_service.save(storage1)
storage_service.save(storage2)


storages = storage_service.find_all()

print("Number of storages:", len(storages))

for storage in storages:
    print(storage.location, storage.capacity)