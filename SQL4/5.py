import os
os.system("cls")

from mysql import connector

mydb = connector.connect(
    host = "localhost",
    user="root",
    password="1234",
    database="dars_db"
)

cursor =  mydb.cursor()

name = input("Ism/familya: ")

query = f"""
  SELECT * FROM users
  WHERE first_name like "%{name}%" OR last_name like "%{name}%";
"""

cursor.execute(query)
jadval = cursor.fetchall()
for i in jadval:
    print(i)