from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, NaiveDatetime

from app.common.enums.transaction_type import FinancialTransactionTypeEnum
from app.common.schema_out_mixin import OrmModeMixin, OutMixin


class FinancialTransactionBase(OrmModeMixin, BaseModel):
    amount: Decimal = Field(..., gt=0, examples=[100.00, 2500.50])
    description: Optional[str] = Field(
        default=None, max_length=120, examples=["Grocery shopping", "Salary payment"]
    )
    transaction_type: FinancialTransactionTypeEnum
    statement_id: int


class FinancialTransactionOut(OutMixin, FinancialTransactionBase):
    pass


class FinancialTransactionIn(FinancialTransactionBase):
    pass


class FinancialTransactionListOut(FinancialTransactionBase):
    transaction_type: FinancialTransactionTypeEnum
    description: Optional[str] = Field(
        default=None, max_length=120, examples=["Grocery shopping", "Salary payment"]
    )
    amount: Decimal = Field(..., gt=0, examples=[100.00, 2500.50])
    created_at: NaiveDatetime
