from db_init import Session,Person02

session = Session()
# 不常用 
# person = session.query(Person02).filter(Person02.id==2).first()
# person.address = "bbb"

# 常用
person = session.query(Person02).filter(Person02.id==2).update({"address":"ccc"})
session.commit() 