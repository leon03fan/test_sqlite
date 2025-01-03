import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Mapped,mapped_column


engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    birthday:Mapped[datetime.datetime]

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)




















