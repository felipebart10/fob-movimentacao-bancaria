from fastapi import APIRouter

from app.schemas.auth import LoginIn
from app.security import sign_jwt
from app.schemas.auth import LoginOut

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login", response_model=LoginOut)
async def login(data: LoginIn):
    return sign_jwt(user_id=data.user_id)