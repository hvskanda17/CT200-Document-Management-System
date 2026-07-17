from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(
    os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
)

db = client["ct200_db"]

generated_collection = db["generated_qa"]