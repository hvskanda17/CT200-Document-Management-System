from fastapi import FastAPI

app = FastAPI(
    title="CT-200 Document Management API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "CT200 Backend Running Successfully"
    }