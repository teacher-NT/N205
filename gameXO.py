from random import choice
import os

def bosh_doska_hosil_qil():
    """
    3x3 o'lchamli ro'yxat hosil qiladi
    :param 
        None - hech narsa qaytarmaydi
    :return 
        list - Hosil bo'lgan ro'yxatni qaytaradi
    """
    doska = [1,2,3,4,5,6,7,8,9]
    return doska
    
def doskani_korsat(doska):
    """
    Doskani ekranga chiqaradi
    :param 
        doska
    :return
        None - hech narsa qaytarmaydi
    """
    count = 0
    print("+-----------+")
    for i in range(9):
        print("|", doska[i], end=" ")
        count += 1
        if count%3 == 0:
            print("|\n+-----------+")

def foydalanuvchi_tanlasin(doska):
    """
    Foydalanuvchidan raqamni so'rab doskani o'zgartiradi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    if not bosh_maydonlar(doska):
        return
    n = int(input("Siz tanlang: "))
    if 1 <= n <=9:
        if n in doska:
            doska[doska.index(n)] = 'O'
        else:
            print("Bo'sh katak tanlang!!!")
            return foydalanuvchi_tanlasin(doska)
    else:
        print("Xato son kiritildi!!!")
        return foydalanuvchi_tanlasin(doska)

def bosh_maydonlar(doska):
    """
    doskadagi bo'sh raqamlar ro'yxatini qaytaradi, ya'ni
    (0 va X bo'lmagan raqamlarni) qaytaradi 
    :param 
        doska
    :return 
        list - raqamlardan iborat bir o'lchamli roy'xat
    """
    result = []
    for i in doska:
        if str(i) not in ["X", "O"]:
            result.append(i)
    return result
     
def golib_bormi(doska, belgi):
    """
    G'olib borligini aniqlaydi
    :param 
        doska
        blegi - X yoki 0. X - Kompyuter, 0 - foydalanuvchi
    :return
        bool - True agar g'olib mavjud bo'lsa, False g'olib bo'lmasa
    """
    if doska[0]==belgi and doska[1]==belgi and doska[2]==belgi:
        return True
    elif doska[3]==doska[4]==doska[5] == belgi:
        return True 
    elif doska[6]==doska[7]==doska[8] == belgi:
        return True
    elif doska[0]==doska[3]==doska[6] == belgi:
        return True
    elif doska[1]==doska[4]==doska[7] == belgi:
        return True
    elif doska[2]==doska[5]==doska[8] == belgi:
        return True
    elif doska[0]==doska[4]==doska[8] == belgi:
        return True
    elif doska[2]==doska[4]==doska[6] == belgi:
        return True
    return False
    
def kompyuter_tanlasin(doska):
    """
    Kompyuter qolgan raqamlar orasidan tasodifiy tanlab,
    usha raqam o'niga X belgisini qo'yadi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    free_space = bosh_maydonlar(doska)
    if free_space:
        x = choice(free_space)
        doska[x-1] = "X"

doska = bosh_doska_hosil_qil()

while bosh_maydonlar(doska):
    os.system("cls")
    kompyuter_tanlasin(doska)
    doskani_korsat(doska)
    if golib_bormi(doska, "X"):
        doskani_korsat(doska)
        print("Kompyuter yutdi!!!")
        break
    foydalanuvchi_tanlasin(doska)
    if golib_bormi(doska, "O"):
        print("Siz yutdingiz!!!")
        break
else:
    print("Durrang!!!")