import os
os.system("cls")

class Flyable:
    def fly(self):
        print("Flying...")

class Swimable:
    def swim(self):
        print("Swimming...")


class Duck(Flyable, Swimable):
    def run(self):
        print("Running...")

duck1 = Duck()
duck1.fly()
duck1.swim()
duck1.run()