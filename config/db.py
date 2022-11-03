from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:cima@localhost:5432/cima")
meta = MetaData()
connection = engine.connect()