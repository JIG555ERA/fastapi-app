from fastapi import FastAPI;

app = FastAPI()

@app.get('/')
def home():
    return {
        "success": True,
        "message": "Server running"
    }
