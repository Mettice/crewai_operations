from fastapi import FastAPI
from app.api.routes.tickets import router as tickets_router
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment":settings.app_env,
        "app_name":settings.app_name
    }


app.include_router(tickets_router)