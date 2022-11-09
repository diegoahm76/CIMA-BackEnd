from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Float, Text
from config.db import meta

MMAMA0004View = Table("28-MMAMA0004", meta, 
    Column("car", Text), 
    Column("cant_arboles", Integer),
    Column("porc_avance", Float))