from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, SmallInteger
from config.db import meta

MunicipioTable = Table("00-Municipio", meta, 
    Column("coddpto", SmallInteger),
    Column("nombredpto", String),
    Column("codmncpio", Integer),
    Column("nombremncpio", String))