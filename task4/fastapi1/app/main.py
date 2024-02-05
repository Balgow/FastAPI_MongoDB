from fastapi import FastAPI, HTTPException
import httpx
from .dependencies import get_api_url

app = FastAPI()

@app.get("/")
async def home():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{get_api_url()}/")
            return response.json()
        except:
            pass
