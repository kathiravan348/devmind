from fastapi import FastAPI

app = FastAPI(title="DevMind API")

@app.get("/health")
def health_check():
    return {"status": "ok"}