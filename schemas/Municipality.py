from pydantic import BaseModel

class MunicipioModel(BaseModel):
    coddpto: int
    nombredpto: str
    codmncpio: int
    nombremncpio: str

class typeValueModel(BaseModel):
    strId: int
    label: str

class MunicipalityObjectModel(BaseModel):
    departments: list[typeValueModel]
    municipalities: list[typeValueModel]