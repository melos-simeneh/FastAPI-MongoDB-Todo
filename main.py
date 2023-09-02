from fastapi import FastAPI 

app=FastAPI()

from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb://localhost:27017/")
try:
    client.admin.command("ping")
    print("MongoDB connected")
except Exception as e:
    print(e)