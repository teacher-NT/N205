import os
os.system("cls")

import json



filename = 'famous_people_200_uzbek.json'
with open(filename) as file:
    data = json.load(file)

def search():
    name = input("Ism kiriting: ")
    for i in data:
        if name.lower() == i['name'].lower():
            print("Ismi:", i['name'])
            print("Tug'ilgan sanasi:", i['birth_date'])
            print("Tug'ilgan joyi:", i['birth_place'])
            print("Ma'lumot:", i['description'])
            break
    else:
        print("Ma'lumot topilmadi...")


def add():
    person = {
        "name": input("Ism kiriting: "),
        "birth_date": input("Tug'ilgan sana: "),
        "birth_place": input("Tug'ilgan joy: "),
        "description": input("Ma'lumot: ")
    }
    data.append(person)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        print("Ma'lumot qo'shildi!")
    
def main():
    while True:
        n = int(input("1. Qidirish.\n2. Qo'shish\n0. Chiqish\n>>> "))
        if n == 1:
            search()
        elif n == 2:
            add()
        else:
            break

main()

