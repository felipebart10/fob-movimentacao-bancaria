from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db
from app.controllers.statement import statement_router
from app.controllers.transaction import transaction_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan,title="Movimentação bancária API", version="1.0.0")
app.include_router(statement_router)
app.include_router(transaction_router)