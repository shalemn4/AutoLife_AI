from database.db import tasks_collection

def schedule_task(task, time):
    tasks_collection.insert_one({"task": task, "time": time})
    return {"task": task, "time": time}

def get_tasks():
    return list(tasks_collection.find({}, {"_id": 0})) 