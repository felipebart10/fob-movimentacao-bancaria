from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, Integer

class BaseModel(DeclarativeBase):
    """Base model with common fields for all tables."""
    id: Mapped[Integer] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(nullable=False, default="CURRENT_TIMESTAMP")
    updated_at: Mapped[DateTime] = mapped_column(nullable=False, onupdate="CURRENT_TIMESTAMP", default="CURRENT_TIMESTAMP")
