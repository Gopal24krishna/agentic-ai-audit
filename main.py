from dotenv import load_dotenv
import os

load_dotenv()

print("OpenAI Key Loaded:", bool(os.getenv("OPENAI_API_KEY")))
print("AWS Region:", os.getenv("AWS_REGION"))
print("DB Name:", os.getenv("DB_NAME"))
