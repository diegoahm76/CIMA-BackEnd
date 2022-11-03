from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Float
from config.db import meta

MMAMA0001View = Table("28-MMAMA0001", meta, 
    Column("longitud", Float), 
    Column("latitud", Float),
    Column("anio", Float),
    Column("cantidad_arboles", Integer))