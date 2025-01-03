import sqlalchemy
from sqlalchemy import create_engine
import datetime


engine = create_engine('sqlite:///test.db', echo=True)
meta_data = sqlalchemy.MetaData()

# 创建空表
person = sqlalchemy.Table('person', meta_data,
                         sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
                         sqlalchemy.Column('name', sqlalchemy.String(255), unique=True, nullable=False),
                         sqlalchemy.Column('birthday', sqlalchemy.Date)
                         )

meta_data.create_all(engine)



# 插入一条记录
# person_insert = person.insert()
# print(person_insert)
# insert_tom = person_insert.values(name='tom02', birthday=datetime.date(1990, 1, 1))


# with engine.connect() as connection:
#     result = connection.execute(insert_tom)
#     connection.commit()
#     print(f"result:{result}")
#     print(f"primarykey:{result.inserted_primary_key}")
#     print(f"primarykey_rows:{result.inserted_primary_key_rows}")


# 插入多条记录
person_insert = person.insert()

with engine.connect() as connection:
    result = connection.execute(person_insert,[
        {'name':'tom05','birthday':datetime.date(1999, 2, 1)},
        {'name':'jerry05','birthday':datetime.date(1999, 3, 1)},
        {'name':'jack05','birthday':datetime.date(1999, 4, 1)}
    ])
    connection.commit()
    # 判断插入是否成功
    if result.rowcount > 0:
        print("插入成功")
    else:
        print("插入失败")
    print(f"result:{result}")
    print(f"primarykey_rows:{result.inserted_primary_key_rows}")









