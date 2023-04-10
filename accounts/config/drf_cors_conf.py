import os
from dotenv import load_dotenv

load_dotenv()
#Configure CORS
CORS_ALLOWED_ORIGINS = [
    os.environ.get("FRONTEND_DOMAIN", "http://localhost:3000"),  # Replace with your Next.js frontend domain
]
CORS_ALLOW_CREDENTIALS = True