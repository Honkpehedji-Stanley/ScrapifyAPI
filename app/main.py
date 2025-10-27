from fastapi import FastAPI, HTTPException
from app.scraper import scrape_quotes
from app.models import Quote
from typing import List

app = FastAPI(
    title="ScrapifyAPI",
    description="A simple FastAPI service that scrapes quotes from a demo website.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to ScrapifyAPI 👋"}

@app.get("/api/quotes", response_model=List[Quote])
def get_quotes():
    try:
        quotes = scrape_quotes()
        return quotes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
