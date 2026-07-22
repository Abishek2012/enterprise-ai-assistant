from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome, Abishek! Enterprise AI Assistant is running successfully."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }