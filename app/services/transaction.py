
from app.schemas.transaction import FinancialTransactionIn, FinancialTransactionOut
from app.models.transaction import FinancialTransaction
from sqlalchemy.ext.asyncio import AsyncSession

class FinancialTransactionService:
    async def post_transaction(self, transaction_data: FinancialTransactionIn, session: AsyncSession) -> FinancialTransactionOut:
        transaction = FinancialTransaction(**transaction_data.model_dump())
        session.add(transaction)
        await session.commit()
        await session.refresh(transaction)
        return FinancialTransactionOut.model_validate(transaction)

