from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from data.connection import engine

# Create the SQLAlchemy engine
  # Replace 'your_database_uri' with the actual URI for your database

# Create a separate MetaData object
metadata = MetaData(bind=engine)

Base = declarative_base(metadata=metadata)  # Associate the MetaData object with the Base class

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'user' not in metadata.tables:
            Base.metadata.create_all(engine)
