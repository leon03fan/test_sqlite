import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite:///test.db', echo=True)
meta_data = sqlalchemy.MetaData()

t_department = sqlalchemy.Table('department', meta_data,
                               sqlalchemy.Column('dept_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
                               sqlalchemy.Column('name', sqlalchemy.String(255), unique=True, nullable=False),
                               )
t_employee = sqlalchemy.Table('employee', meta_data,
                              sqlalchemy.Column('emp_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
                              sqlalchemy.Column('name', sqlalchemy.String(255), unique=True, nullable=False),
                              sqlalchemy.Column('dept_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('department.dept_id'))
                              )


meta_data.create_all(engine)
