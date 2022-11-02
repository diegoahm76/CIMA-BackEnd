from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:cima@localhost:5432/paises")
meta = MetaData()
connection = engine.connect()