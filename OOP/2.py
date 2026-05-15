import os
os.system("cls")

class Car:
    brand = "BMW"
    model = "M8"
    price = 200000
    color = 'black'

    def show_info(self):
        print(f"{self.brand} {self.model} {self.price} {self.color}")

    def change_price(self, new):
        self.price = new

car1 = Car()
# print(car1.brand)
# print(car1.model)
car1.show_info()
car1.change_price(150000)
car1.show_info()

car2 = Car()
car2.show_info()
car2.change_price(300000)
car2.show_info()