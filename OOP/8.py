import os
os.system("cls")

class Flyable:
    def fly(self):
        print("Flying...")

class Swimable:
    def swim(self):
        print("Swimming...")


class People:
    def swim(self):
        print("People can swim...")


class Duck( Flyable, Swimable, People):
    def run(self):
        print("Running...")

class Bird(Duck):
    def fly(self):
        print("Bird is flying...")

bird1 =  Bird()
bird1.fly()
bird1.run()
bird1.swim()