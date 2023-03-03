import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
PASSWORD = os.getenv("PASSWORD")
