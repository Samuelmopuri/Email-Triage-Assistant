import os
import json
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from openai import OpenAI
from dotenv import load_dotenv

# Load API keys from your .env file
load_dotenv()

# --- CONFIGURATION ---
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
# This pulls the key from your .env file for security
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gmail_service():
    """Handles OAuth2.0 authentication with Google."""
    creds = None
    # token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def scale_down_triage(email_body):
    """
    The AI Brain: Performs 'ScaleDown' summarization, 
    Priority Scoring, and Sentiment (Vibe) Analysis.
    """
    prompt = f"""
    Act as an AI Executive Chief of Staff. Analyze the following email thread:
    TEXT: {email_body[:3500]} 

    Analyze the content and the 'Vibe' of the sender.
    Return a structured JSON response with these EXACT fields:
    1. summary: A 1-sentence recap of the thread (85% compression).
    2. priority_score: 1-10 (10 is critical).
    3. sender_vibe: (e.g., Frustrated, Formal, Excited, Passive-Aggressive).
    4. heat_map: (Cold, Warm, Hot) based on relationship urgency.
    5. meeting_info: Extracted dates/times or "None".
    6. smart_draft: A 1-sentence response that MATCHES the sender's tone.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Using the latest model for better sentiment detection
            messages=[
                {"role": "system", "content": "You are a professional triage assistant. Output ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"error": f"AI Processing failed: {str(e)}"}

def main():
    print("🚀 Initializing Email Triage Assistant...")
    
    try:
        service = get_gmail_service()
    except Exception as e:
        print(f"❌ Error connecting to Gmail: {e}")
        return

    # Fetch the 5 most recent unread emails
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread", maxResults=5).execute()
    messages = results.get('messages', [])

    if not messages:
        print("✅ Inbox Zero! No unread emails found.")
        return

    print(f"📥 Found {len(messages)} unread emails. Analyzing...\n")

    for msg in messages:
        # Fetch the full email content
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        
        # We use 'snippet' for speed, but for full threads, you'd parse the payload
        content = msg_data.get('snippet', '')
        
        print(f"🔍 Analyzing Message ID: {msg['id']}...")
        report = scale_down_triage(content)
        
        if "error" in report:
            print(f"⚠️ {report['error']}")
            continue

        # Terminal Output
        print(f"--- TRIAGE REPORT ---")
        print(f"📌 SUMMARY: {report.get('summary')}")
        print(f"🔥 PRIORITY: {report.get('priority_score')}/10 [{report.get('heat_map')}]")
        print(f"🎭 SENDER VIBE: {report.get('sender_vibe')}")
        print(f"📅 MEETINGS: {report.get('meeting_info')}")
        print(f"✍️ AI DRAFT: \"{report.get('smart_draft')}\"")
        print("-" * 30)

if __name__ == '__main__':
    main()
