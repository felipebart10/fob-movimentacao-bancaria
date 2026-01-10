from fastapi import APIRouter, Depends
from app.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.statement import StatementOut
from app.services.statement import StatementService

statement_router = APIRouter(prefix="/statements", tags=["statements"])

service = StatementService()

@statement_router.post("/", response_model=StatementOut)
async def create_statement(session: AsyncSession = Depends(get_session)) -> StatementOut:
    return await service.post_statement(session)