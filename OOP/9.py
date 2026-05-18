import os
os.system("cls")

class Animal:
    def run(self):
        print("Running...")
    
    def eat(self):
        print("Eating...")


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Pinguin(Animal):
    pass

d1 = Dog()
c1 = Cat()
p1 = Pinguin()

d1.eat()
d1.run()

c1.eat()
c1.run()

p1.eat()
p1.eat()