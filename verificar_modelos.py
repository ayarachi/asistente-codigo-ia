from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("🔍 Listando modelos disponibles en tu cuenta...\n")

try:
    models = client.models.list()
    print("✅ Modelos disponibles:")
    for model in models:
        print(f"  - {model.name}")
except Exception as e:
    print(f"❌ Error: {e}")