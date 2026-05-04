🚀 AutoLife AI – Smart Daily Life Automation System

AutoLife AI is an AI-powered personal assistant that simplifies daily life by combining task management, expense tracking, reminders, and scheduling into a single unified platform. It uses a multi-agent architecture to intelligently process user commands and automate actions.

🌟 Overview
AutoLife AI transforms how users manage their daily activities by enabling natural language interaction instead of manual input across multiple apps.
Manage tasks, reminders, and expenses in one place
Use AI to automate workflows
Reduce cognitive load and improve productivity

🧠 Key Features
AI-powered natural language assistant
Multi-agent system (Expense, Reminder, Scheduler, Admin)
Core Agent for intelligent decision-making
MCP-based task routing system
Expense tracking and management
Smart reminders and scheduling
Real-time automation workflow
API-based modular architecture
Scalable backend design

🏗️ Architecture
The system follows a multi-agent modular architecture:
User → API Layer → Core Agent (AI) → MCP Router → Specialized Agents → Database → Response
Core Agent processes user intent
MCP layer routes tasks to appropriate agents
Agents execute tasks and store data

⚙️ Tech Stack
Backend
Python (FastAPI)
Uvicorn
AI Layer
ADK-style logic for intent understanding
Database
MongoDB (Prototype)
Scalable to AlloyDB
Cloud & Deployment
Google Cloud Run (Serverless deployment)
Google Cloud Build (CI/CD)
Docker (Containerization)

🚀 Deployment (Google Cloud Run)
1. Set Project
gcloud config set project autolife-ai-project
2. Build Image
gcloud builds submit --tag gcr.io/autolife-ai-project/autolife-ai
3. Deploy
gcloud run deploy autolife-ai \
--image gcr.io/autolife-ai-project/autolife-ai \
--region asia-south1 \
--platform managed \
--allow-unauthenticated
4. Access

After deployment:

https://autolife-ai-xxxx.a.run.app
📡 API Endpoints
Core
GET / → Health check
POST /ask-ai → AI-based command processing
Expense
POST /add-expense
GET /get-expenses
Admin (Bills)
POST /add-bill
GET /get-bills
Scheduler
POST /schedule-task
GET /get-tasks
Reminder
POST /add-reminder
GET /get-reminders
Workflow
POST /pay-bill-workflow → Multi-agent automation
Dashboard
GET /dashboard-summary

🔄 Workflow
User sends command (e.g., “Add expense 200”)
Core Agent processes intent
MCP routes to correct agent
Agent executes task
Data stored in database
Response returned to user

📈 Future Enhancements
Voice assistant integration
Mobile app (Android/iOS)
Bank API integration for real-time finance tracking
AI insights and analytics dashboard
Multi-user and team collaboration
