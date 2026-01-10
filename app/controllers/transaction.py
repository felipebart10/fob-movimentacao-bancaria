from fastapi import APIRouter, Depends
from app.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.transaction import FinancialTransactionIn, FinancialTransactionOut
from app.services.transaction import FinancialTransactionService

transaction_router = APIRouter(prefix="/transaction", tags=["transaction"])

service = FinancialTransactionService()

@transaction_router.post("/", response_model=FinancialTransactionOut)
async def create_transaction(transaction_data: FinancialTransactionIn, session: AsyncSession = Depends(get_session)) -> FinancialTransactionOut:
    return await service.post_transaction(transaction_data, session)