from fastapi import APIRouter
from app.api import auth

router = APIRouter()
router.include_router(auth.router, tags=["auth"])
