from db_init import Session,Customer
import datetime

session = Session()
c = Customer(name="Jack", birthday=datetime.date(1999, 4, 1))

session.add(c)
session.commit()