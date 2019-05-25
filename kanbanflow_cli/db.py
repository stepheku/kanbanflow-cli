from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os.path

db_path = os.path.join('.', 'db', 'kanbanflow_cli.db')
engine = create_engine(db_path, echo=True)
Base = declarative_base()


class School(Base):

    __tablename__ = "woot"

    id = Column(Integer, primary_key=True)
    name = Column(String)  


    def __init__(self, name):

        self.name = name    


Base.metadata.create_all(engine)