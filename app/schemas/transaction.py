from pydantic import BaseModel, PositiveFloat
from app.common.enums.transaction_type import FinancialTransactionTypeEnum
from app.common.schema_out_mixin import OrmModeMixin, OutMixin

class FinancialTransactionBase(OrmModeMixin, BaseModel):
    amount: PositiveFloat
    description: str
    transaction_type: FinancialTransactionTypeEnum
    statement_id: int

class FinancialTransactionOut(OutMixin, FinancialTransactionBase):
    pass

class FinancialTransactionIn(FinancialTransactionBase):
    pass
