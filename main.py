from fastapi import FastAPI
from src.api.question_router import router

app = FastAPI(
    title="Product Documentation AI Assistant",
    description="An API for answering product-related questions",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Product Documentation AI Assistant API is running"
    }
    
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "API is working properly"
    }