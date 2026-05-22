import os
os.system("cls")

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def kick(self):
        pass

    @abstractmethod
    def jump(self):
        pass

class Spiderman(Player):
    def __init__(self,  n, xp):
        self.name = n
        self.xp = xp
    
    def run(self):
        print(f"{self.name} is running...")
    
    def kick(self):
        print(f"{self.name} is kicking...")
    
    def jump(self):
        print(f"{self.name} is jumping...")

s1 = Spiderman('Suhrob', 500)
print(s1.name)
