from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String
from config.db import meta

PoblacionTable = Table("Poblacion", meta, 
    Column("tipodocumento", String),
    Column("numerodocumento", String),
    Column("primernombre", String),
    Column("segundonombre", String),
    Column("primerapellido", String),
    Column("segundoapellido", String),
    Column("correo", String),
    Column("telefono", String),
    Column("direccion", String))