import os
os.system("cls")

class Person:
    def __init__(self, n,a,m):
        self.name = n
        self.age = a
        self.nation = m
    
    def __str__(self):
        return f"{self.name} {self.age} {self.nation}"

p1 = Person("Doston", 20, "Uzbek")
print(p1)