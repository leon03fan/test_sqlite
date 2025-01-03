import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship


engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    dept_id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    create_time:Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now, nullable=False)
    def __repr__(self):
        return f"Department(id={self.dept_id}, name={self.name}, create_time={self.create_time})"

class Employee(Base):
    __tablename__ = "employees"

    emp_id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    dept_id:Mapped[int] = mapped_column(ForeignKey("departments.dept_id"))
    name:Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    birthday:Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now, nullable=False)

    department: Mapped[Department] = relationship()

    def __repr__(self):
        return f"Employee(id={self.emp_id}, name={self.name}, create_time={self.birthday}, department_id={self.department_id})"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)




















