import os
os.system("cls")

class Person:
    def __init__(self, n,a,m,s):
        self.name = n
        self.age = a
        self.nation = m
        self.skills = s
    
    def __str__(self):
        return f"{self.name} {self.age} {self.nation}"

    def __gt__(self, n):
        return self.age > n
    
    def __lt__(self, n):
        return self.age < n
    
    def __eq__(self, n):
        return self.age == n
    
    def __add__(self, n):
        self.age += n
    
    def  __sub__(self, n):
        self.age -= n
    
    def __mul__(self, n):
        self.name *= n
    
    def __contains__(self, item):
        for i in self.skills:
            if item.lower() == i.lower():
                return True
        return False

p1 = Person("Doston", 20, "Uzbek", ['Python', 'Russion', 'English', 'Swimming', 'Sleeping'])
a = 12
# print(a > 5)
# print(p1 < 25)
# print(p1 > 25)
# print(p1 == 20)

if "english" in p1:
    print("Yes")
else:
    print("No")