from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

import app.common.exceptions as exc
from app.controllers.statement import statement_router
from app.controllers.transaction import transaction_router
from app.controllers.auth import auth_router
from app.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan, title="Movimentação bancária API", version="1.0.0")
app.include_router(statement_router)
app.include_router(transaction_router)
app.include_router(auth_router)


@app.exception_handler(exc.ForeignKeyNotFoundError)
async def foreign_key_not_found_exception_handler(
    request, exc: exc.ForeignKeyNotFoundError
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


@app.exception_handler(exc.InsufficientFundsError)
async def insufficient_funds_exception_handler(
    request, exc: exc.InsufficientFundsError
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )
