Email Triage Assistant 📧 🤖
The Email Triage Assistant is an intelligent automation agent designed to solve "Inbox Fatigue." By integrating the Gmail API with GPT-4o, it transforms a cluttered inbox into a prioritized, actionable dashboard.

🌟 The Unique Edge: "EQ Triage"
Unlike standard filters that look for keywords like "Urgent," this agent uses LLM-based Sentiment Analysis to understand the "Vibe" of the sender. It identifies if a sender is Frustrated, Formal, or Excited and builds a Relationship Heat-Map to prioritize emails based on emotional stakes and professional urgency.

🚀 Key Features
ScaleDown Summarization: Compresses massive threads (50+ messages) into 1-sentence actionable summaries, achieving ~85% text reduction.

Priority Scoring: A weighted 1-10 ranking based on sender intent, sentiment, and urgency.

Meeting Extraction: Automatically identifies dates and times for potential scheduling.

Tone-Matched Drafting: Generates professional response templates that mirror the sender’s "vibe" (e.g., empathetic replies for frustrated senders).

🛠️ Technical Stack
Language: Python 3.9+

APIs: Gmail API (Google Workspace), OpenAI GPT-4o

Authentication: OAuth 2.0

Environment: python-dotenv, google-api-python-client

⚙️ Installation & Setup
Clone the Repository

Bash
git clone https:
cd email-triage-assistant
Configuration

Place your credentials.json (from Google Cloud Console) in the root directory.

Create a .env file and add your OpenAI key:

Code snippet
OPENAI_API_KEY=your_actual_key_here
Install Dependencies

Bash
pip install -r requirements.txt
Run the Assistant

Bash
python triage.py
🧠 System Architecture
Ingestion: Connects to the Gmail API to retrieve unread message payloads.

Processing (ScaleDown): Strips redundant metadata and repetitive signatures to maximize LLM efficiency.

Analysis: Performs sentiment detection and priority scoring in a single, high-speed AI pass.

Output: Generates a structured Triage Report including a "Vibe" check and suggested draft.

🛡️ Security & Privacy
OAuth 2.0: Secure handshake with Google; tokens are stored locally in token.json.

Minimal Scoping: Uses gmail.readonly to ensure the assistant cannot delete or modify your emails.

Local Secrets: API keys and credentials are excluded from version control via .gitignore.

🤝 License
This project is licensed under the MIT License - see the LICENSE file for details.
