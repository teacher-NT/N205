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

cursor.execute("SELECT * FROM users WHERE posts_count between 500 and 1000;")

# jadval = cursor.fetchall()
# for i in jadval:
    # print(i)

# jadval = cursor.fetchone()
# print(jadval)

jadval = cursor.fetchmany(5)
for i in jadval:
    print(i)
