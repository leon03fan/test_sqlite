from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()

class Person02(Base):
    __tablename__ = 'person02'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    birthday = Column(Date)
    address = Column(String(255))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)




