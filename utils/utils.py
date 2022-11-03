from schemas.MMAMA0001 import MMAMA0001Model, GeoJsonModel, FeaturesModel

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
