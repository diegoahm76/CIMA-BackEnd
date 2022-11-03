from fastapi import APIRouter
from config.db import connection
from models.MMAMA0001 import MMAMA0001View
from schemas.MMAMA0001 import MMAMA0001Model, GeoJsonModel
from utils.utils import setDataGeoJson

tree = APIRouter()

@tree.get("/trees", response_model=GeoJsonModel, tags=["Trees"])
def get_tree_list():
    treeList = connection.execute(MMAMA0001View.select()).fetchall()
    geoJsonTrees = setDataGeoJson("FeatureCollection", "Feature", "Point", treeList)
    return geoJsonTrees

@tree.get("/trees/{year}", response_model=GeoJsonModel, tags=["Trees"])
def get_tree_list_by_year(year: float):
    treesForYear = connection.execute(MMAMA0001View.select().where(MMAMA0001View.c.anio == year)).fetchall()
    geoJsonTrees = setDataGeoJson("FeatureCollection", "Feature", "Point", treesForYear)
    return geoJsonTrees