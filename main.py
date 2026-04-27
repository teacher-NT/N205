import os
os.system("cls")

car = {
    "brand": "Chevrolet",
    "model": "Cobalt",
    "rang": ["oq", "qora", "qizil", "ko'k","yashil"],
    "narx": 12000,
    "ish-turi": "Taksi",
    "probeg": 80_000,
}
# print(car["yil"])
# print(car.get('yil', "topilmadi"))

# print(list(car.keys()))

# print(list(car.values()))

# k = car.pop("probeg")
# print(car)
# print(k)

# car2 = car.copy()
# print(car2)

# print(car.items())
# for i,j in car.items():
#     print(i, j)

# car.clear()
# print(car)

# k = car.popitem()
# print(k)
# print(car)

# car['narx'] = 9000
# car['ish-turi'] = 'dastavka'
# car['probeg'] = 100000

car.update({"narx": 9000, 'ish-turi':'dastavka', 'probeg':100000})
print(car)