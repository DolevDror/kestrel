from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from .database import Database
from typing_extensions import Annotated

from .database_functions import database_router
from .auth import check_key 

load_dotenv()

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    Database.initialize()

    yield

    Database.close_connection()


app = FastAPI(
    title="1678 Kestrel",
    description="API for connecting to the 1678 scouting database",
    version="1.0.0",
    lifespan=db_lifespan
)

app.include_router(database_router.router,
                   tags=["Database"], 
                   prefix="/database",
                   dependencies=[Depends(check_key)])

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


