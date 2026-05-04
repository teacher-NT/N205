import os
os.system("cls")

import random as rd

n = rd.randint(1,100)
print(n)

# m = rd.uniform(1, 10)
# print(m)

names = ['Samandar', 'Sherali', 'Doston', 'Begzod', 'Suhrob']
print(rd.choice(names))
print(rd.choices(names, k=2))
print(rd.sample(names, k=2))

rd.shuffle(names)
print(names)