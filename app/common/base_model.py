from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class BaseModel(DeclarativeBase):
    """Base model with common fields for all tables."""
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(nullable=False, onupdate=datetime.now(), default=datetime.now())
