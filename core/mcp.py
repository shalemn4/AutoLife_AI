from agents import finance, admin, scheduler, reminder

tools = {
    "add_expense": finance.add_expense,
    "add_bill": admin.add_bill,
    "schedule_task": scheduler.schedule_task,
    "add_reminder": reminder.add_reminder
}

def execute_tool(tool_name, *args):
    if tool_name in tools:
        return tools[tool_name](*args)
    return {"error": "Tool not found"}