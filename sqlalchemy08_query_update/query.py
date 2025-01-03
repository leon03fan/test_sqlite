from db_init import Session, Person02

session = Session()

# result = session.query(Person02).all()
# for person in result:
#     print(f"name:{person.name},birthday:{person.birthday}")

# result = session.query(Person02).filter(Person02.name=="tom02")
# for person in result:
#     print(f"name:{person.name},birthday:{person.birthday}")

# 多条记录只返回第一条，究竟那一条是第一条 取决于排序条件
# person = session.query(Person02).filter(Person02.name.like("tom%")).first()
# if person :
#     print(f"name:{person.name},birthday:{person.birthday}")

# one要求结果集中有且只有一条记录 否则会报错
person = session.query(Person02).filter(Person02.name.like("tom%")).one()

# scalar是在one的基础上加工得到的 没有数据的时候 不会报错
person = session.query(Person02).filter(Person02.name.like("tom%")).scalar()

# 上面几种方法显示使用不是很多
