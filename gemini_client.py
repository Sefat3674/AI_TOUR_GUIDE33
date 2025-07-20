import os

API_KEY = os.getenv("GEMINI_KEY")

import requests
import os

API_KEY = os.getenv("GEMINI_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
HEADERS = {"Content-Type": "application/json"}

def ask_gemini(prompt):
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    res = requests.post(URL, headers=HEADERS, json=payload)
    return res.json()['candidates'][0]['content']['parts'][0]['text']

def translate_to_bangla(english_text):
    prompt = f"Translate this to Bengali:\\n\\n{english_text}"
    return ask_gemini(prompt)
