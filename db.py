import json
from pymongo import MongoClient

name = "SungWoon"
id = "cds07016"
password = "qq009261"
client = MongoClient("mongodb://localhost")

print("DB Connect")

db = client.testdb

collection = db.user

userdata = {
    "username" : name,
    "id" : id,
    "password" : password
}


users = []

for post in collection.find():
    users.append(post)

print(users)