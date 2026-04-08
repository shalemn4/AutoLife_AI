from database.db import expenses_collection
from utils.helpers import clean_mongo

def add_expense(item, amount):
    expense = {"item": item, "amount": amount}
    expenses_collection.insert_one(expense)


    return {
        "item": item,
        "amount": amount
    }


def get_expenses():
    data = list(expenses_collection.find())
    return clean_mongo(data)