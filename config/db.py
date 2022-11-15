from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:LNHmWoJJ57TtHlYDgcDb@sig-database.c1ur1zqj7pwl.us-east-1.rds.amazonaws.com:5432/cima")
# engine = create_engine("postgresql://postgres:cima@localhost:5432/cima")
meta = MetaData()
connection = engine.connect()