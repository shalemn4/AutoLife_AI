from core.gemini import ask_gemini
from core.mcp import execute_tool

def process_request(user_input: str):

    prompt = f"""
    You are an AI assistant.

    Choose EXACTLY one tool:
    - add_expense
    - add_bill
    - schedule_task
    - add_reminder

    ONLY return the tool name. No explanation.

    User input: {user_input}
    """

    decision = ask_gemini(prompt).strip().lower()
    print("AI RAW:", decision)

    if "add_expense" in decision:
        return execute_tool("add_expense", "ai_expense", 100)

    elif "add_bill" in decision:
        return execute_tool("add_bill", "electricity", 1500)

    elif "schedule_task" in decision:
        return execute_tool("schedule_task", "task from ai", "tomorrow")
    
    elif "add_reminder" in decision:
        prompt2 = f"""
        Extract reminder message and time from this:
        
        "{user_input}"
          Return in format:
          message: <text>
          time: <time>
          """
        result = ask_gemini(prompt2)
    print("AI EXTRACT:", result)

    # simple parsing
    message = "Reminder"
    time = "tomorrow"

    if "message:" in result and "time:" in result:
        try:
            parts = result.split("\n")
            message = parts[0].split("message:")[1].strip()
            time = parts[1].split("time:")[1].strip()
        except:
            pass

    return execute_tool("add_reminder", message, time)

    return {"message": f"AI unclear: {decision}"}