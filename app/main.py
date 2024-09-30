from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Movie Summarizer API")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Movie Summarizer API"}