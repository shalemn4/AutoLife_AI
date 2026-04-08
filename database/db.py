from pymongo import MongoClient

client = MongoClient("mongodb+srv://Agent:agent123@database.nxptbvm.mongodb.net/?appName=Database")
db = client["autolife"]

expenses_collection = db["expenses"]
bills_collection = db["bills"]
tasks_collection = db["tasks"]
reminders_collection = db["reminders"]