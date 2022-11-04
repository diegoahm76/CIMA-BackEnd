from fastapi import APIRouter
from config.db import connection
from models.MMAMA0001 import MMAMA0001View
from models.MMAMA0002356 import MMAMA0002356View
from schemas.MMAMA0001 import GeoJsonModel
from utils.utils import setDataGeoJson

tree = APIRouter()



@tree.get("/trees/getByYear/{year}", response_model=GeoJsonModel, tags=["Trees"])
def get_tree_list_by_year(year: float):
    treesForYear = connection.execute(MMAMA0001View.select().where(MMAMA0001View.c.anio == year)).fetchall()
    geoJsonTrees = setDataGeoJson("FeatureCollection", "Feature", "Point", treesForYear)
    return geoJsonTrees

@tree.get("/trees/getByDepartment/{dptoId}", tags=["Trees"])
def get_tree_list_by_department(dptoId: str):
    treesForDepartment = connection.execute(MMAMA0002356View.select().where(MMAMA0002356View.c.departamento == dptoId)).fetchall()
    return treesForDepartment

@tree.get("/trees/getByMunicipality/{mpioId}", tags=["Trees"])
def get_tree_list_by_department(mpioId: str):
    treesForMunicipality = connection.execute(MMAMA0002356View.select().where(MMAMA0002356View.c.municipio == mpioId)).fetchall()
    return treesForMunicipality