from fastapi import APIRouter, Response
from config.db import connection
from models.Poblacion import PoblacionTable
from schemas.Population import PopulationModel
from utils.utils import setModelPerson
from starlette.status import HTTP_400_BAD_REQUEST 

population = APIRouter()

@population.post("/population/createPerson", tags=["Population"])
def create_person(newPerson: PopulationModel):
    personInDB = connection.execute(PoblacionTable.select().where(PoblacionTable.c.numerodocumento == newPerson.numerodocumento)).first()
    if personInDB == None:
        connection.execute(PoblacionTable.insert().values(setModelPerson(newPerson)))
        return "El registro se ha guardado con éxito."
    return Response(status_code=HTTP_400_BAD_REQUEST, content="El registro que intenta guardar ya existe en base de datos.")