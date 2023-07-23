import os
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
db_string = os.getenv('DB_PORT') or "mongodb+srv://mohitmb0208:testmongodb@cluster0.b7mbr.mongodb.net/?authMechanism=SCRAM-SHA-1"
client = MongoClient(db_string)
db = client['pythonDB']


import os
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Retrieve the database connection details from environment variables
db_user = os.getenv("LOGIN_ID")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

# Construct the database connection URI
SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

# Create the SQLAlchemy engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
sqdb = Session()

Base = declarative_base()

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
        if 'user' not in engine.table_names():
            Base.metadata.create_all(engine)

