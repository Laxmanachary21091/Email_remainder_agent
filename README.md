📧 Intelligent Email Agent (CrewAI + OpenAI)

An intelligent Email Agent built using the CrewAI framework and OpenAI LLM, designed to automatically read your emails, extract important information (meetings, deadlines, action items), store them in a database, and send you voice reminders.

🚀 Features

📥 Reads incoming emails via Gmail IMAP API

🧠 Uses OpenAI LLM for semantic understanding of email content

⚙️ Detects meetings, appointments, and important events automatically

🗓️ Creates structured reminders (date, time, description, notes)

💾 Stores reminders and extracted info in a local SQLite database

🔊 Speaks reminders aloud using text-to-speech (voice mode)

🧰 Built with CrewAI for modular agent design

🪄 Fully customizable and extendable

🧩 Folder Structure
📦 email-agent/
├── app.py                # Main entry point (runs the agent)
├── email_reader.py       # Reads emails using IMAP
├── email_parser.py       # Extracts important data using OpenAI
├── database.py           # Handles SQLite storage
├── voice_reminder.py     # Converts reminders to voice
├── .env                  # Stores credentials and API keys
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/email-agent.git
cd email-agent

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in your project root and add the following:

OPENAI_API_KEY=your_openai_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
VOICE_API_KEY=your_voice_api_key   # Optional
DB_PATH=email_agent.db

🔑 Gmail App Password Setup

Go to Google App Passwords

Select “Mail” as the app and “Other” → name it EmailAgent

Copy the generated password

Paste it into .env as EMAIL_PASS

▶️ Run the Agent
python app.py

🧠 Example Input & Output
Input Email:
Subject: HR Meeting
Body:
Hi,
We have a meeting today at 2:00 PM with HR.
Thanks,
John

Output JSON:
{
  "is_important": true,
  "summary": "Meeting today at 2:00 PM with HR.",
  "reminder": {
    "date": "2025-10-18",
    "time": "14:00",
    "title": "HR Meeting",
    "notes": ""
  },
  "store_data": {
    "sender": "HR",
    "subject": "HR Meeting",
    "body": "Hi, We have a meeting today at 2:00 PM with HR.",
    "event_type": "meeting",
    "event_time": "14:00",
    "event_date": "2025-10-18"
  }
}


🔊 The agent will also speak:

“Reminder: HR meeting today at 2 PM.”

🧰 Tech Stack

Python 3.10+

CrewAI Framework

OpenAI API (LLM)

Flask (Backend)

SQLite (Database)

pyttsx3 / TTS (Voice)

💡 Future Enhancements

🔁 Integrate Google Calendar API for automatic event syncing

📩 Add support for Outlook and Yahoo mail

🧭 Dashboard to view upcoming reminders

🕹️ Streamlit interface for user interaction

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to improve.# Email_remainder_agent
