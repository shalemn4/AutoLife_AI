from database.db import bills_collection

def add_bill(name, amount):
    bills_collection.insert_one({"name": name, "amount": amount})
    return {"name": name, "amount": amount}

def get_bills():
    return list(bills_collection.find({}, {"_id": 0}))