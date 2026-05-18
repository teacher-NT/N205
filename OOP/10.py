import os
os.system("cls")

class A:
    def func1(self):
        print("This is A!")

class B:
    def func1(self):
        print("This is B!")

class C(A, B):
    pass

class D(A, B):
    pass

class E(D, C):
    pass

e1 = E()
e1.func1()
# print(E.__mro__)