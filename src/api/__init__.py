from fastapi import APIRouter
from src.api.scheduler import router as scheduler_router
main_router = APIRouter()

main_router.include_router(scheduler_router)