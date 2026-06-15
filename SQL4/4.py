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

query = """
   DELETE FROM users
   WHERE first_name LIKE "b%";
"""

cursor.execute(query)
mydb.commit()
print(f"{cursor.rowcount} ta qator o'zgardi")
