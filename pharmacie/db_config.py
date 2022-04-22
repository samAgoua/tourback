import databases
import sqlalchemy
import ormar

DATABASE_URL = "sqlite:///pharm.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata