from typing import Optional
from pydantic import BaseModel

class MMAMA0001Model(BaseModel): 
    longitud: float
    latitud: float
    anio: Optional[float]
    cantidad_arboles: int

class GeometryModel(BaseModel):
    type: str
    coordinates: list[float]

class PropertiesModel(BaseModel):
    anio: float
    x: float
    y: float

class FeaturesModel(BaseModel):
    type: str
    geometry: GeometryModel
    properties: PropertiesModel

class GeoJsonModel(BaseModel):
    type: str
    features: list[FeaturesModel]

    