import os
os.system("cls")

ages = [19,23,15,31,18]

def func1(n):
    return n+1
lst2 = list(map(func1, ages))
print(lst2)

lst2 = list(map(lambda n: n+1, ages))
print(lst2)


