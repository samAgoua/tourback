import sqlalchemy
from .db_config import DATABASE_URL

engine = sqlalchemy.create_engine(DATABASE_URL)