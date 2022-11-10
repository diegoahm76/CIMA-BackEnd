from fastapi import APIRouter
from config.db import connection
from models.Municipio import MunicipioTable
from utils.utils import setDataMunicipality
from schemas.Municipality import MunicipalityObjectModel

typeValues = APIRouter()

@typeValues.get("/typeValues/getMunicipalityList", response_model=MunicipalityObjectModel, tags=["TypeValues"])
def get_municipality_list():
    municipalityList = connection.execute(MunicipioTable.select()).fetchall()
    data = setDataMunicipality(municipalityList)
    return data