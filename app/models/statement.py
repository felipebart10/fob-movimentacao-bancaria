from app.common.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from sqlalchemy import Numeric
from typing import List


class Statement(BaseModel):
    """Model representing a financial statement."""
    __tablename__ = "statements"
    position: Mapped[Decimal] = mapped_column(Numeric(scale=2), nullable=False)
    transactions: Mapped[List["FinancialTransaction"]] = relationship(
        back_populates="statement", cascade="all, delete-orphan"
    )
