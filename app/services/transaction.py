from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import app.common.exceptions as exc
from app.models.statement import Statement
from app.models.transaction import FinancialTransaction
from app.schemas.transaction import (FinancialTransactionIn,
                                     FinancialTransactionOut)


class FinancialTransactionService:
    """Service for managing financial transactions.

    This service handles the creation and persistence of financial transaction records,
    including validation against related statements.
    """

    async def post_transaction(
        self, transaction_data: FinancialTransactionIn, session: AsyncSession
    ) -> FinancialTransactionOut:
        transaction = FinancialTransaction(**transaction_data.model_dump())
        statement = (
            await session.execute(
                select(Statement).where(Statement.id == transaction.statement_id)
            )
        ).scalar_one_or_none()
        if not statement:
            raise exc.ForeignKeyNotFoundError("Statement not found.")

        else:
            if (
                statement.position - transaction.amount < 0
                and transaction.transaction_type.value == "debit"
            ):
                raise exc.InsufficientFundsError(
                    "Insufficient funds for this debit transaction."
                )
            else:
                if transaction.transaction_type.value == "debit":
                    statement.position -= transaction.amount
                else:
                    statement.position += transaction.amount

        session.add(transaction)
        await session.commit()
        await session.refresh(transaction)
        return FinancialTransactionOut.model_validate(transaction)
