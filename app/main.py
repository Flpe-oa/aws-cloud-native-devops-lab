
from fastapi import FastAPI

app = FastAPI(
    title="PulseOps",
    description="Cloud Native DevOps Lab - Service Health API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "PulseOps",
        "description": "Service Health API",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/status")
def status():
    return {
        "application": "PulseOps",
        "status": "running",
        "environment": "development",
    }

