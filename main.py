import os
os.system("cls")

with open("image.jpeg", "rb") as file:
    baytlar = list(file.read())
    # for i in baytlar:
    #     print(i, end=" ")

    print(f"\n{len(baytlar)} ta raqam")
