from app.common.base_model import BaseModel
from app.common.enums.transaction_type import FinancialTransactionTypeEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, ForeignKey, Enum
from decimal import Decimal


class FinancialTransaction(BaseModel):
    """Model representing a financial transaction."""
    __tablename__ = "financial_transactions"
    amount: Mapped[Decimal] = mapped_column(Numeric(scale=2), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True, max_length=120)
    transaction_type: Mapped[FinancialTransactionTypeEnum] = mapped_column(Enum(FinancialTransactionTypeEnum), nullable=False)
    statement_id: Mapped[int] = mapped_column(ForeignKey("statements.id"), nullable=False)

    statement: Mapped["Statement"] = relationship(back_populates="transactions")