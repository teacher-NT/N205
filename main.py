import os
os.system("cls")

car = {
    "brand": "Chevrolet",
    "model": "Cobalt",
    "rang": "oq",
    "narx": 12000,
    "ish-turi": "Taksi",
    "probeg": 80_000,
    "rang": "qora"
}

car["brand"] = "GM"
car['yil'] = 2023
print(car['model'], car["brand"], sep=", ")
print(car)