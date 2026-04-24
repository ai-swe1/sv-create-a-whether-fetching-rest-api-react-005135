from fastapi import APIRouter
from fastapi import HTTPException
import requests
from app.config import OPENWEATHERMAP_API_KEY

router = APIRouter()

@router.get("/weather")
def read_weather():
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London&appid={OPENWEATHERMAP_API_KEY}')
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))