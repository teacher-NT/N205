import os
os.system("cls")

class A:
    def move(self):
        print("A is moving...")

class B(A):
    def move(self):
        print("B is moving...")

a1 = A()
b1 = B()

a1.move()
b1.move()