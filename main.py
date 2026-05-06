import os
os.system("cls")
import json

# users= [
#     {
#         "username": "ozodoov__",
#         "followers":500,
#         "following": 100,
#         "posts_count": 0
#     },
#     {
#         "username": "suhrob",
#         "followers":500,
#         "following": 1200,
#         "posts_count": 6000
#     },
#     {
#         "username": "Sherali",
#         "followers":220,
#         "following": 340,
#         "posts_count": 32
#     },
#     {
#         "username": "Ayubxon",
#         "followers":5000,
#         "following": 280,
#         "posts_count": 40
#     }
# ]

# file = open("users.json", "w")
# json.dump(users, file, indent=4)

file = open("users.txt")
users = json.load(file)
print(users)