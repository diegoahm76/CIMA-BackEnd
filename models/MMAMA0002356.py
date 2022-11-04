from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Float, Date, Text
from config.db import meta

MMAMA0002356View = Table("28-MMAMA0002-3-5-6", meta, 
    Column("anio", Float),
    Column("mes", Float),
    Column("fec_siemb", Date),
    Column("orga", Text),
    Column("departamento", Text),
    Column("municipio", Text),
    Column("cp", Text),
    Column("cant_arboles", Integer),
    Column("departamento_f", Text),
    Column("municipio_f", Text))