from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

rioModelDb = Table("mexico_hidrografia", meta, 
    Column("gid", Integer, primary_key=True), 
    Column("nombre", String(40)),
    Column("cuenca", String(40)))