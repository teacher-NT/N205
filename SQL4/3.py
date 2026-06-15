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
   UPDATE users
   SET posts_count=700, followers=1200000
   WHERE user_id = 31;
"""

cursor.execute(query)
mydb.commit()
print(f"{cursor.rowcount} ta qator o'zgardi")
