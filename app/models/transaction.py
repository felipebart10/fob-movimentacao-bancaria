from app.commons.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.statement import Statement
else:
    Statement = None

class Transaction(BaseModel):
    """Model representing a financial transaction."""
    amount: Mapped[Float] = mapped_column(precision=2, nullable=False)
    description: Mapped[String] = mapped_column(nullable=True, max_length=120)
    statement_id: Mapped[int] = mapped_column(ForeignKey("statements.id"), nullable=False)

    statement: Mapped["Statement"] = relationship(back_populates="transactions")