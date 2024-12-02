import requests
import os
from dotenv import load_dotenv


load_dotenv()
session_cookie = os.getenv("SESSION_COOKIE")

def get_input(day: int) -> str:
    url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "YourCustomUserAgent (email@example.com)"  # Optional but polite
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to get input: {response.status_code} - {response.text}")
