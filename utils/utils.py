from schemas.MMAMA0001 import MMAMA0001Model, GeoJsonModel, FeaturesModel
from schemas.Municipality import MunicipioModel, typeValueModel, MunicipalityObjectModel

def setDataGeoJson(type: str, typeFeature: str, typeGeometry: str, data: list[MMAMA0001Model]):
    features: list[FeaturesModel] = []
    for item in data:
        feature: FeaturesModel = {
            "type": typeFeature,
            "geometry": {
                "type": typeGeometry,
                "coordinates": [item.longitud, item.latitud]
            },
            "properties": {
                "anio": item.anio,
                "x": item.longitud,
                "y": item.latitud
            }
        }
        features.append(feature)
    geojsonData: GeoJsonModel = {
        "type": type,
        "features": features
    }
    return geojsonData

def setDataMunicipality(data: list[MunicipioModel]):
    departmentList: list[typeValueModel] = []
    municipalityList: list[typeValueModel] = []
    for item in data:
        departmentList.append({"strId": item.coddpto, "label": item.nombredpto})
        municipalityList.append({"strId": item.codmncpio, "label": item.nombremncpio})

    listTypeValue: MunicipalityObjectModel = {
        "departments": list({item['strId']:item for item in departmentList}.values()),
        "municipalities": municipalityList
    }

    return listTypeValue
