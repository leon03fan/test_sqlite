import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite:///test.db', echo=True)
meta_data = sqlalchemy.MetaData()

t_person = sqlalchemy.Table('person', meta_data,
                         sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
                         sqlalchemy.Column('name', sqlalchemy.String(255), unique=True, nullable=False),
                         sqlalchemy.Column('birthday', sqlalchemy.Date)
                         )


meta_data.create_all(engine)
