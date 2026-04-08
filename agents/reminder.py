from database.db import reminders_collection

def add_reminder(message, time):
    reminders_collection.insert_one({"message": message, "time": time})
    return {"message": message, "time": time}

def get_reminders():
    return list(reminders_collection.find({}, {"_id": 0}))