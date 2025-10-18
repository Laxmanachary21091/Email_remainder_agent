from email_reader import ImapReader
from agent import analyze_email
from database import init_db, save_reminder
from voice_reminder import speak_reminder
from dotenv import load_dotenv
import os

load_dotenv()

init_db()
reader = ImapReader(
    host=os.getenv("IMAP_SERVER"),
    port=int(os.getenv("IMAP_PORT")),
    username=os.getenv("EMAIL_USER"),
    password=os.getenv("EMAIL_PASS")
)

emails = reader.fetch_unseen()
for e in emails:
    result = analyze_email(e)
    print("📩 Analyzed:", result)

    if result["is_important"]:
        save_reminder(result)
        print("✅ Reminder saved to database.")
        speak_reminder(result["summary"], result["reminder"]["time"])
