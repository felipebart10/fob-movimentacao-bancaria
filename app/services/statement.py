from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.statement import Statement
from app.models.transaction import FinancialTransaction
from app.schemas.statement import StatementOut
from app.schemas.transaction import FinancialTransactionListOut


class StatementService:
    async def post_statement(self, session: AsyncSession) -> StatementOut:
        statement = Statement(position=0.0)
        session.add(statement)
        await session.commit()
        await session.refresh(statement)
        return StatementOut.from_orm(statement)

    async def get_statement_by_id(
        self, statement_id: int, session: AsyncSession
    ) -> StatementOut | None:
        result = await session.execute(
            select(Statement).where(Statement.id == statement_id)
        )
        statement = result.scalar_one_or_none()
        if statement:
            return StatementOut.model_validate(statement)
        return None

    async def delete_statement(self, statement_id: int, session: AsyncSession) -> None:
        result = await session.execute(
            select(Statement).where(Statement.id == statement_id)
        )
        statement = result.scalar_one_or_none()
        if statement:
            await session.delete(statement)
            await session.commit()
        return None

    async def get_transaction_list(
        self, statement_id: int, session: AsyncSession
    ) -> list[FinancialTransactionListOut]:
        result = await session.execute(
            select(FinancialTransaction).where(
                FinancialTransaction.statement_id == statement_id
            )
        )
        transactions = result.scalars().all()
        return [
            FinancialTransactionListOut.model_validate(transaction)
            for transaction in transactions
        ]
