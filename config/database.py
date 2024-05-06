from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = ""
uri2 = ""
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# this will try to connect to a todo_db database, if it doesn't exist, it will be created
db = client.todo_db

collection_name = db["todo_collection"]