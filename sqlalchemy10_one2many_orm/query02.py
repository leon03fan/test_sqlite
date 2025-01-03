from db_init02 import Session, Department, Employee
import datetime

def insert_records(session):
    dept1 = Department(name="X")

    emp1 = Employee(name="lyon", birthday=datetime.datetime(1980, 1, 1), department=dept1)
    session.add(emp1)
    session.commit()

session = Session()
insert_records(session)
