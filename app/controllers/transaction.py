from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.transaction import (FinancialTransactionIn,
                                     FinancialTransactionOut)
from app.services.transaction import FinancialTransactionService

transaction_router = APIRouter(prefix="/transaction", tags=["transaction"])

service = FinancialTransactionService()


@transaction_router.post(
    "/",
    response_model=FinancialTransactionOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create transaction",
    description="Create a new financial transaction associated with a statement.",
    operation_id="createTransaction",
    responses={
        201: {"description": "Transaction created successfully."},
        400: {"description": "Invalid transaction data."},
        404: {"description": "Related statement not found."},
    },
)
async def create_transaction(
    transaction_data: FinancialTransactionIn = Body(...),
    session: AsyncSession = Depends(get_session),
) -> FinancialTransactionOut:
    return await service.post_transaction(transaction_data, session)
