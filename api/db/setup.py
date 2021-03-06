import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

mongodb_url = os.environ.get("MONGO_DB_CONNECTION_STRING")

client = MongoClient(mongodb_url)
db = client["pytho-gcp"]


def db_connect():
    try:
        client.admin.command("ismaster")
        print("Connected to database")
    except ConnectionFailure:
        print("Failed to connect to database")
