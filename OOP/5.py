import os
os.system("cls")

class Animal:
    def __init__(self, type, color, name):
        self.name = name
        self.color = color
        self.type = type

    def sound(self):
        print("Animal is speaking...")

# a1 = Animal("BullDog", 'black', 'rex')

class Dog(Animal):
    pass

dog1 = Dog('Dalmatin', 'oq-qora', 'mitti')
dog1.sound()