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
    INSERT INTO users(user_id, username, first_name, last_name, posts_count, followers, followings, joined)
    VALUES
    (31, "suhrobjon", 'Suhrob', "Yormamatov", 0, 244, 894, "2025-03-19");
"""

cursor.execute(query)
mydb.commit()
print(f"{cursor.rowcount} ta qator o'zgardi")
