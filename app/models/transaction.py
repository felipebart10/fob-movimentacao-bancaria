from decimal import Decimal

from sqlalchemy import Enum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.base_model import BaseModel
from app.common.enums.transaction_type import FinancialTransactionTypeEnum


class FinancialTransaction(BaseModel):
    """Model representing a financial transaction."""

    __tablename__ = "financial_transactions"
    amount: Mapped[Decimal] = mapped_column(Numeric(scale=2), nullable=False)
    description: Mapped[str] = mapped_column(String(length=120), nullable=True)
    transaction_type: Mapped[FinancialTransactionTypeEnum] = mapped_column(
        Enum(FinancialTransactionTypeEnum), nullable=False
    )
    statement_id: Mapped[int] = mapped_column(
        ForeignKey("statements.id"), nullable=False
    )

    statement: Mapped["Statement"] = relationship(back_populates="transactions")
