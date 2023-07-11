from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import JSON, Integer, Column, String, MetaData


PG_DSN = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5440/hw2_asyncio"
engine = create_async_engine(PG_DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
print(PG_DSN)


class Swapipeople(Base):
    __tablename__ = 'swapi people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    films = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    species = Column(String)
    skin_color = Column(String)
    mass = Column(String)
    homeworld = Column(String)
    height = Column(String)
    hair_color = Column(String)
    gender = Column(String)
    starships = Column(String)
    vehicles = Column(String)




