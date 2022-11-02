from typing import List
from fastapi import APIRouter
from config.db import connection
from models.rioModel import rioModelDb
from schemas.rio import Rio
rio = APIRouter()
# esto es un comentario de prueba
@rio.get("/Rio", response_model=list[Rio], tags=["Rios"])
def get_rios():
    return connection.execute(rioModelDb.select()).fetchall()

@rio.get("/Rio/{id}", response_model=Rio, tags=["Rios"])
def get_rio_by_Id(id: int):
    return connection.execute(rioModelDb.select().where(rioModelDb.c.gid == id)).first()