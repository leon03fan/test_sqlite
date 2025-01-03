import sqlalchemy
from sqlalchemy import create_engine

print(sqlalchemy.__version__)


# **************************************************
# 连接数据库
# **************************************************
engine = create_engine('sqlite:///test.db', echo=True)
Connection = engine.connect()

query = sqlalchemy.text('select * from tb01')
result = Connection.execute(query)

for row in result:
    print(row)

Connection.close()
engine.dispose()










