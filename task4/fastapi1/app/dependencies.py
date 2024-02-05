import os

def get_api_url() -> str:
    return os.getenv("FASTAPI2_URL", "http://localhost:8002")
