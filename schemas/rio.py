from pydantic import BaseModel
from typing import Optional

class Rio(BaseModel): 
    gid: Optional[int]
    nombre: Optional[str]
    cuenca: Optional[str]