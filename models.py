from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import JSON, Integer, Column, String, MetaData
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# connection = psycopg2.connect(user="postgres")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = connection.cursor()
#sql_create_database = cursor.execute('create database hw_asyncio')
# cursor.close()
# connection.close()

metadata = MetaData()
PG_DSN = "postgresql+asyncpg://postgres@127.0.0.1:5440/hw1_asyncio"
engine = create_async_engine(PG_DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
print(PG_DSN)


class SwapiPeople(Base):
    __tablename__ = "swapi_people"

    id = Column(Integer, primary_key=True)
    #json = Column(JSON)
    # # films = Column(JSON)
    name = Column(String)





