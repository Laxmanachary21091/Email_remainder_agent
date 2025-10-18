import schedule, time
from datetime import datetime
from voice_reminder import speak_reminder

def send_reminder(summary, time_str):
    print(f"🔔 Reminder: {summary} at {time_str}")
    speak_reminder(summary, time_str)

def start_scheduler():
    # Demo reminder every 1 minute
    schedule.every(1).minutes.do(lambda: send_reminder("HR Meeting - Internship Documents", datetime.now().strftime("%H:%M")))

    while True:
        schedule.run_pending()
        time.sleep(10)
