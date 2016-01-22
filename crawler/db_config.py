from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import Column, Integer, String, create_engine
from elasticsearch import Elasticsearch
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

es=Elasticsearch()
es.indices.create(index='vacancies', ignore=400)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()

Session = sessionmaker(bind=engine)

class Vacancy(Base):
	__tablename__='vacancies'
	id = Column(Integer, primary_key=True)
	company_name = Column(String)
	image_path = Column(String)
	place = Column(String)
	title = Column(String)
	source = Column(String)

Base.metadata.create_all(engine)