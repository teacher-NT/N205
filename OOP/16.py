import os
os.system("cls")

class BankAccount:
    def __init__(self, n, b):
        self.name = n
        self.__balance = b

    
b1 = BankAccount("Suhrob", 1000)
print(b1.name)
# b1.__balance = 2000
print(b1.__balance)