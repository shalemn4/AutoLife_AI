import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [item, setItem] = useState("");
  const [amount, setAmount] = useState("");
  const [expenses, setExpenses] = useState([]);
  const [reminders, setReminders] = useState([]);
  const [aiResponse, setAiResponse] = useState("");

  // ADD EXPENSE
  const addExpense = async () => {
    if (!item || !amount) return;

    await fetch("http://127.0.0.1:8000/add-expense", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ item, amount: Number(amount) }),
    });

    setItem("");
    setAmount("");
    getExpenses();
  };

  // GET EXPENSES
  const getExpenses = async () => {
    const res = await fetch("http://127.0.0.1:8000/get-expenses");
    const data = await res.json();
    setExpenses(data);
  };

  // GET REMINDERS
  const getReminders = async () => {
    const res = await fetch("http://127.0.0.1:8000/get-reminders");
    const data = await res.json();
    setReminders(data);
  };

  // ASK AI
  const askAI = async () => {
    if (!query) return;

    const res = await fetch("http://127.0.0.1:8000/ask-ai", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
    });

    const data = await res.json();

    // 🔥 CLEAN RESPONSE FORMAT
    if (data.message && data.time) {
      setAiResponse(`✅ Reminder set: "${data.message}" at ${data.time}`);
    } else if (data.item && data.amount) {
      setAiResponse(`💰 Expense added: ${data.item} - ₹${data.amount}`);
    } else if (data.name && data.amount) {
      setAiResponse(`🧾 Bill added: ${data.name} - ₹${data.amount}`);
    } else {
      setAiResponse("⚡ Action completed");
    }

    // refresh everything
    getExpenses();
    getReminders();
  };

  return (
    <div style={{ padding: 30, maxWidth: 600, margin: "auto" }}>
      <h1>🚀 AutoLife AI</h1>

      {/* ADD EXPENSE */}
      <h2>Add Expense</h2>
      <div style={{ display: "flex", gap: 10 }}>
        <input
          placeholder="Item"
          value={item}
          onChange={(e) => setItem(e.target.value)}
        />
        <input
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <button onClick={addExpense}>Add</button>
      </div>

      {/* AI */}
      <h2>Ask AI</h2>
      <div style={{ display: "flex", gap: 10 }}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Type command..."
        />
        <button onClick={askAI}>Run</button>
      </div>

      {/* CLEAN AI RESPONSE */}
      <p style={{ background: "#222", padding: 10, borderRadius: 6 }}>
        <b>AI Response:</b> {aiResponse}
      </p>

      {/* EXPENSES */}
      <h2>Expenses</h2>
      <button onClick={getExpenses}>Refresh</button>
      <ul>
        {expenses.map((e, i) => (
          <li key={i}>
            {e.item} - ₹{e.amount}
          </li>
        ))}
      </ul>

      {/* REMINDERS */}
      <h2>Reminders</h2>
      <button onClick={getReminders}>Refresh</button>
      <ul>
        {reminders.map((r, i) => (
          <li key={i}>
            {r.message} - {r.time}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;