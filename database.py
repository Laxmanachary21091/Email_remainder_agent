import sqlite3

def init_db():
    conn = sqlite3.connect("email_data.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        subject TEXT,
        summary TEXT,
        date TEXT,
        time TEXT,
        title TEXT,
        notes TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_reminder(data):
    conn = sqlite3.connect("email_data.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO reminders (sender, subject, summary, date, time, title, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["store_data"].get("sender", ""),
        data["store_data"].get("subject", ""),
        data.get("summary", ""),
        data["reminder"].get("date", ""),
        data["reminder"].get("time", ""),
        data["reminder"].get("title", ""),
        data["reminder"].get("notes", "")
    ))
    conn.commit()
    conn.close()
