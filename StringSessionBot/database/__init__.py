from pymongo import MongoClient
from env import DATABASE_URL

count_ = 0
client = None
db = None

def start():
    global client, db
    if DATABASE_URL == "":
        global count_
        if count_ < 1:
            count_ += 1
            print("Database URL not provided..\nBut this time I won't stop 😉")
        return
    # Establish MongoDB connection
    client = MongoClient(DATABASE_URL)
    db = client.get_default_database()  # Get the default database or specify db name
    
if DATABASE_URL != "":
    start()

# Now `db` can be used to interact with the MongoDB database
