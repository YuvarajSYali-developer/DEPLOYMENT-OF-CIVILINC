from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import ml_model, endpoints as api_endpoints, auth
from app.db.init_db import init_db
import os

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Create models directory if it doesn't exist
os.makedirs(settings.MODEL_DIR, exist_ok=True)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=settings.API_V1_STR, tags=["auth"])
app.include_router(ml_model.router, prefix=f"{settings.API_V1_STR}/ml", tags=["ml"])
app.include_router(api_endpoints.router, prefix=settings.API_V1_STR, tags=["projects", "complaints", "services", "events"])

@app.on_event("startup")
async def startup_event():
    init_db()
    from app.core.ml_service import MLService
    ml_service = MLService()
    ml_service._load_models()

@app.get("/")
async def root():
    return {
        "message": "Welcome to CivilInc API",
        "version": settings.VERSION,
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }
