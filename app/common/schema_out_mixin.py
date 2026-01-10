from pydantic import BaseModel, NaiveDatetime

class OrmModeMixin(BaseModel):
    class Config:
        from_attributes = True
        orm_mode = True

class OutMixin(BaseModel):
    id: int
    created_at: NaiveDatetime
    updated_at: NaiveDatetime

    class Config:
        orm_mode = True