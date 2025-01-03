from db_init01 import Session, Department, Employee
import datetime

def insert_records(session):
    dept1 = Department(name="Sales")
    dept2 = Department(name="Marketing")
    session.add(dept1)
    session.add(dept2)
    session.flush()

    emp1 = Employee(name="John Doe", birthday=datetime.datetime(1980, 1, 1), dept_id=dept1.dept_id)
    emp2 = Employee(name="Jane Smith", birthday=datetime.datetime(1985, 2, 15), dept_id=dept2.dept_id)
    session.add(emp1)
    session.add(emp2)
    session.commit()

session = Session()
insert_records(session)
