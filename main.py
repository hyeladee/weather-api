from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import httpx
import time
import os

load_dotenv()  # Load variables from .env

app = FastAPI()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CACHE = {}
CACHE_EXPIRY = 3600

@app.get("/weather")
async def get_weather(city: str):
    now = time.time()
    city_key = city.lower()

    if city_key in CACHE:
        cached_data, timestamp = CACHE[city_key]
        if now - timestamp < CACHE_EXPIRY:
            return cached_data

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        if res.status_code != 200:
            raise HTTPException(status_code=res.status_code, detail="City not found")
        data = res.json()

    CACHE[city_key] = (data, now)
    return data

@app.get("/")
async def root():
    return FileResponse("index.html")