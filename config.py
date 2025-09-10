import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
