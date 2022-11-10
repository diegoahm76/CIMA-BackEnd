from fastapi import APIRouter
from config.db import connection
from models.MMAMA0001 import MMAMA0001View
from models.MMAMA0002356 import MMAMA0002356View
from models.MMAMA0004 import MMAMA0004View
from schemas.MMAMA0001 import GeoJsonModel
from utils.utils import setDataGeoJson

tree = APIRouter()


@tree.get("/trees/getAllTrees", response_model=GeoJsonModel, tags=["Trees"])
def get_tree_list_all():
    treesByYear = connection.execute(MMAMA0001View.select()).fetchall()
    geoJsonTrees = setDataGeoJson("FeatureCollection", "Feature", "Point", treesByYear)
    return geoJsonTrees

@tree.get("/trees/getByYear/{year}", response_model=GeoJsonModel, tags=["Trees"])
def get_tree_list_by_year(year: float):
    treesByYear = connection.execute(MMAMA0001View.select().where(MMAMA0001View.c.anio == year)).fetchall()
    geoJsonTrees = setDataGeoJson("FeatureCollection", "Feature", "Point", treesByYear)
    return geoJsonTrees

@tree.get("/trees/getByDepartment/{dptoId}", tags=["Trees"])
def get_tree_list_by_department(dptoId: str):
    treesByDepartment = connection.execute(MMAMA0002356View.select().where(MMAMA0002356View.c.cod_depto == dptoId)).fetchall()
    return treesByDepartment

@tree.get("/trees/getByMunicipality/{mpioId}", tags=["Trees"])
def get_tree_list_by_municipality(mpioId: int):
    treesByMunicipality = connection.execute(MMAMA0002356View.select().where(MMAMA0002356View.c.cod_mncipio == mpioId)).fetchall()
    return treesByMunicipality

@tree.get("/trees/getByCar/{car}", tags=["Trees"])
def get_tree_list_by_car(car: str):
    treesByCar = connection.execute(MMAMA0004View.select().where(MMAMA0004View.c.car == car)).fetchall()
    return treesByCar