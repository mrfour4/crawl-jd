import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = "mongodb+srv://nono:HDiT4x5DQAuxLKtx@cluster0.9ex6dby.mongodb.net/skill_recommend"
MONGO_DB = os.getenv("MONGO_DB", "skill_recommend")         
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "jobs")  

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]
