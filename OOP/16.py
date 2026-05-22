import os
os.system("cls")

class BankAccount:
    def __init__(self, n, b, p):
        self.name = n
        self.__balance = b
        self._parol = p
    
    def get_balance(self, parol):
        if parol == 'qwerty':
            print(self.__balance)
        else:
            print("Parol xato!")
    def set_balance(self, new, parol):
        if parol == 'qwerty':
            self.__balance = new
            print("Balans o'zgardi")
        else:
            print("Parol xato!")

    
b1 = BankAccount("Suhrob", 1000, "qwerty")
print(b1.name)
# b1.__balance = 2000
# print(b1.__balance)
b1.get_balance("qwerty")
b1.set_balance(1500, "12ewcwe")
# b1.get_balance("qwerty")

print(b1._parol)
