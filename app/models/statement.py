from app.commons.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.transaction import Transaction
else:
    Transaction = None

class Statement(BaseModel):
    """Model representing a financial statement."""
    __tablename__ = "statements"

    position: Mapped[Float] = mapped_column(precision=2, nullable=False)
    transactions: Mapped[List["Transaction"]] = relationship(
        back_populates="statement", cascade="all, delete-orphan"
    )