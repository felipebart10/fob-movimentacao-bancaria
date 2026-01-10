from app.schemas.statement import StatementOut
from app.models.statement import Statement
from sqlalchemy.ext.asyncio import AsyncSession

class StatementService:
    async def post_statement(self, session: AsyncSession) -> StatementOut:
        statement = Statement(position=0.0)
        session.add(statement)
        await session.commit()
        await session.refresh(statement)
        return StatementOut.from_orm(statement)

