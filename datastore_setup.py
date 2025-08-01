from pymongo import MongoClient

# This LOC makes connection to Database
client = MongoClient("mongodb://localhost:27017/")


#This LOC creates or gets the Database
db = client["linq_database"]
collection = db["sample_data"]

# Inserts a sample document to create the database and collection
collection.insert_one({
    "project": "Linq Internship",
    "status": "in-progress",
    "technologies": ["MongoDB", "Python", "React"],
    "owner": {
        "name": "Sumanth",
        "email": "sallurisumanth05@gmail.com"
    }
})


print("Database and collection set up successfully.")
