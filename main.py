from fastapi import FastAPI
from fastapi.responses import JSONResponse
import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"status": "DARDELİK aktif"}

@app.get("/health")
def health():
    return JSONResponse({
        "app": "DARDELİK",
        "plan": "GÜVENLİ",
        "health_score": 82,
        "message": "Plan stabil. Müdahale gerekmiyor.",
        "date": str(datetime.date.today())
    })
