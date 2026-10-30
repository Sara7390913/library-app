from model.storage import Storage
from controller.storage_controller import StorageController

storage_controller = StorageController()

storage1 = Storage(1, "Tehran", 10, [])
storage2 = Storage(2, "Tabriz", 20, [])

storage_controller.save(storage1)
storage_controller.save(storage2)

storages = storage_controller.find_all()

print("Number of storages: ", len(storages))

for storage in storages:
    print(storage.location, storage.capacity)


