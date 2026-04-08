from fastapi import FastAPI
from pydantic import BaseModel
from agents import finance, admin, scheduler, reminder
from core import adk
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Finance APIs
class Expense(BaseModel):
    item: str
    amount: float

@app.post("/add-expense")
def add_expense(exp: Expense):
    data = finance.add_expense(exp.item, exp.amount)
    print("RETURNING:", data)
    return data

@app.get("/get-expenses")
def get_expenses():
    return finance.get_expenses()


# Admin APIs
@app.post("/add-bill")
def add_bill(name: str, amount: float):
    return admin.add_bill(name, amount)

@app.get("/get-bills")
def get_bills():
    return admin.get_bills()


# Scheduler APIs
@app.post("/schedule-task")
def schedule_task(task: str, time: str):
    return scheduler.schedule_task(task, time)

@app.get("/get-tasks")
def get_tasks():
    return scheduler.get_tasks()


# Reminder APIs
@app.post("/add-reminder")
def add_reminder(message: str, time: str):
    return reminder.add_reminder(message, time)

@app.get("/get-reminders")
def get_reminders():
    return reminder.get_reminders()

class QueryRequest(BaseModel):
    query: str
@app.post("/ask-ai")
def ask_ai(request: QueryRequest):
    return adk.process_request(request.query)


# Multi-Agent Workflow
@app.post("/pay-bill-workflow")
def pay_bill_workflow(name: str, amount: float, time: str):

    bill = admin.add_bill(name, amount)
    task = scheduler.schedule_task(f"Pay {name} bill", time)
    expense = finance.add_expense(name, amount)
    rem = reminder.add_reminder(f"Pay {name} bill", time)

    return {
        "message": "Workflow executed 🚀",
        "bill": bill,
        "task": task,
        "expense": expense,
        "reminder": rem
    }


# Dashboard
@app.get("/dashboard-summary")
def dashboard_summary():
    expenses = finance.get_expenses()
    bills = admin.get_bills()
    tasks = scheduler.get_tasks()
    reminders = reminder.get_reminders()

    total_expense = sum(item["amount"] for item in expenses)

    return {
        "total_expenses": total_expense,
        "total_bills": len(bills),
        "total_tasks": len(tasks),
        "total_reminders": len(reminders)
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)