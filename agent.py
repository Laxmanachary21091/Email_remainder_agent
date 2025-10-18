import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_email(email):
    prompt = f"""
You are an intelligent email agent.

Extract all important information from the email below:
Sender: {email['sender']}
Subject: {email['subject']}
Body: {email['body']}

Return ONLY JSON in this format:
{{
  "is_important": true/false,
  "summary": "",
  "reminder": {{
    "date": "",
    "time": "",
    "title": "",
    "notes": ""
  }},
  "store_data": {{}}
}}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        json_output = json.loads(response.choices[0].message.content)
        return json_output
    except:
        return {"is_important": False, "summary": "", "reminder": None, "store_data": {}}
