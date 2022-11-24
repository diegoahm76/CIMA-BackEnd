from typing import Optional
from pydantic import BaseModel

class PopulationModel(BaseModel):
    tipodocumento: str
    numerodocumento: str
    primernombre: str
    segundonombre: Optional[str]
    primerapellido: str
    segundoapellido: Optional[str]
    correo: Optional[str]
    telefono: Optional[str]
    direccion: Optional[str]