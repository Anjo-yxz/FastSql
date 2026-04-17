from dotenv import load_dotenv
import os
from pathlib import Path

def Env():
    base = Path(__file__).resolve().parent.parent
    dotenv = base / "database" / ".env"
    load_dotenv(dotenv_path=dotenv)
    db = os.getenv("db")
    return db