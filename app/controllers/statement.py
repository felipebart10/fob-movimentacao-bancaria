from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.statement import StatementOut
from app.schemas.transaction import FinancialTransactionListOut
from app.services.statement import StatementService
from app.security import login_required

statement_router = APIRouter(prefix="/statements", tags=["statements"])

service = StatementService()


@statement_router.post(
    "/",
    response_model=StatementOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a statement",
    description="Create a new statement with an initial position.",
    operation_id="createStatement",
    responses={
        201: {"description": "Statement created successfully."},
    },
)
async def create_statement(
    session: AsyncSession = Depends(get_session),
) -> StatementOut:
    return await service.post_statement(session)


@statement_router.get(
    "/{statement_id}",
    response_model=StatementOut | None,
    summary="Get a statement",
    description="Retrieve a statement by its ID.",
    operation_id="getStatementById",
    responses={
        200: {"description": "Statement retrieved successfully."},
        404: {"description": "Statement not found."},
    },
    dependencies=[Depends(login_required)],
)
async def get_statement(
    statement_id: int,
    session: AsyncSession = Depends(get_session),
) -> StatementOut | None:
    return await service.get_statement_by_id(statement_id, session)


@statement_router.delete(
    "/{statement_id}",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a statement",
    description="Delete a statement by its ID and return the deleted resource.",
    operation_id="deleteStatement",
    responses={
        204: {"description": "Statement deleted successfully."},
        404: {"description": "Statement not found."},
    },
    dependencies=[Depends(login_required)],
)
async def delete_statement(
    statement_id: int,
    session: AsyncSession = Depends(get_session),
) -> None:
    return await service.delete_statement(statement_id, session)


@statement_router.get(
    "/{statement_id}/transactions",
    response_model=list[FinancialTransactionListOut],
    summary="Get transactions for a statement",
    description="Retrieve all financial transactions associated with a specific statement.",
    operation_id="getTransactionsForStatement",
    responses={
        200: {"description": "Transactions retrieved successfully."},
        404: {"description": "Statement not found."},
    },
    dependencies=[Depends(login_required)],
)
async def get_transactions_for_statement(
    statement_id: int,
    session: AsyncSession = Depends(get_session),
) -> list[FinancialTransactionListOut]:
    return await service.get_transaction_list(statement_id, session)
