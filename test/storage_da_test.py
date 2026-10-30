from model.storage import Storage
from data_access.storage_da import StorageDa

storage_da = StorageDa()

storage1 = Storage(1, "Tehran", 10, [])
storage2 = Storage(2, "Tabriz", 20, [])

storage_da.save(storage1)
storage_da.save(storage2)


storages = storage_da.find_all()

print("Number of storages:", len(storages))

for storage in storages:
    print(storage.location, storage.capacity)