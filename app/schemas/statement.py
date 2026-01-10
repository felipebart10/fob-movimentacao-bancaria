from pydantic import BaseModel, NonNegativeFloat
from app.common.enums.transaction_type import FinancialTransactionTypeEnum
from app.common.schema_out_mixin import OrmModeMixin, OutMixin

class StatementBase(OrmModeMixin, BaseModel):
    position: NonNegativeFloat

class StatementOut(OutMixin, StatementBase):
    pass

class StatementIn(StatementBase):
    pass
