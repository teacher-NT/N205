import os
os.system("cls")

class A:
    def __init__(self, n,s):
        self.name = n
        self.surname = s

class B(A):
    def __init__(self,n, s, a):
        super().__init__(n,s)
        self.age = a
    