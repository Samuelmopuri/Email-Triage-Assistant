# Email-Triage-Assistant
**Email Triage Assistant 📧 🤖**
The Email Triage Assistant is an intelligent inbox management agent designed to automate categorization, prioritize high-value communications, and streamline the path to Inbox Zero. By leveraging LLMs and direct API integrations, it transforms a cluttered inbox into an organized, actionable feed.

🚀 Project Overview
This project implements a sophisticated triage pipeline that goes beyond traditional keyword filters. It uses agentic logic to understand the context of conversations, ensuring that urgent requests are surfaced immediately while routine threads are summarized.

Key Features:
ScaleDown Summarization: Compresses lengthy email threads (50+ messages) into concise, actionable 1-sentence summaries while preserving critical context.

Intelligent Priority Scoring: A weighted analysis system that scores emails from 1-10 based on urgency, sender importance, and sentiment.

Automated Meeting Extraction: Scans incoming mail for dates and times, identifying potential scheduling needs automatically.

Context-Aware Drafting: Generates professional response templates tailored to the specific content of each thread.

Smart Categorization: Automatically assigns emails to "Smart Folders" like Finance, Meetings, or Social.

🛠️ Technical Stack
Language: Python 3.9+

APIs: Gmail API (Google Workspace), OpenAI GPT-4o

Authentication: OAuth 2.0

Core Libraries: google-api-python-client, openai, python-dotenv
