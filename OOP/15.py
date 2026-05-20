import os
os.system("cls")

class Person:
    def __init__(self, n,a,m):
        self.name = n
        self.age  = a
        self.nation = m

    def __gt__(self, n):
        return self.age > n
    
class Employee:
    def  __init__(self, n,a,m,s,r):
        self.name = n
        self.age= a
        self.nation = m
        self.salary = s
        self.rank = r

    def __gt__(self, n):
        return self.salary > n
    
p1 = Person("Suhrob", 19, "Uzbek")
print(p1 > 100)

e1 = Employee('Diyorbek', 25, 'Uzbek', 500, 'Developer')
print(e1 > 100)